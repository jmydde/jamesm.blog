---
title: "*sshole: How a 256-Byte Limit Let Attackers Log Into Locked Accounts on Alpine Linux"
date: 2026-11-06T16:10:00+00:00
draft: false
tags: ["security", "linux", "docker", "devops", "2026"]
description: "A 2012 change in musl's crypt(), a 2016 OpenSSH hardening patch and a password longer than 256 bytes combine into an authentication bypass on Alpine and other musl systems. It was exploited within hours of disclosure. Here is how the bug works and what to do about it."
---

## TL;DR

- **\*sshole** (CVE-2026-123158) is an OpenSSH authentication bypass. On Linux systems built on the **musl** C library with **PAM disabled**, a password longer than 256 bytes can log in to an account that is supposed to have no usable password
- The cause is not one bug but three reasonable-looking decisions made years apart, in two different projects, that only fail when combined
- The fix is **OpenSSH 10.6p2**, released on 5 November 2026. If you cannot patch yet, set `PasswordAuthentication no` and restart sshd
- Threat intelligence firm Previdian reported exploitation in the wild, including root on a honeypot, less than nine hours after the CVE was published
- Updating the package is not enough on its own: the running sshd has to be restarted

Most vulnerability stories involve a flaw in cryptography or a memory-safety bug in a parser. This one is more interesting, and in some ways more uncomfortable, because nothing in it is obviously wrong. Each component did something defensible. The hole only exists in the gap between them.

## What is affected

According to [BleepingComputer's report](https://www.bleepingcomputer.com/news/security/openssh-flaw-lets-attackers-log-into-password-disabled-linux-accounts/), the bug needs all of these conditions to be true:

- OpenSSH running on a **musl-based** Linux system, such as Alpine Linux, OpenWrt, Buildroot or Yocto builds
- **PAM authentication disabled**, which is the default in Alpine's `openssh-server` package
- SSH **password authentication enabled**
- At least one account whose password field is just `*` (the Unix convention for "no password can ever match this"), and another account with a valid hash

Systems using glibc (Debian, Ubuntu, Fedora) are not affected, and neither are setups that use PAM. That matters, because it means the distribution name alone does not tell you whether you are exposed. A Docker image based on Alpine that runs sshd is in scope. A Debian server is not.

The research was done by Özgün Kültekin, and the write-up and interactive demo are at [sshhole.com](https://sshhole.com/).

## How three good decisions made a bug

The root cause is a chain of three changes.

**1. musl's `crypt()` returns `*` on failure (2012).** According to the researcher's write-up, musl's `crypt()` once returned NULL when hashing failed, and a 2012 change made it return the string `"*"` instead. That is a sensible-looking choice: a `*` can never match a real hash, so a failed hash should never authenticate anyone.

**2. musl's SHA-512 crypt gets a 256-byte password limit.** Roughly three weeks later, per the same write-up, musl added a limit of 256 bytes for passwords in its SHA-512 implementation, as protection against denial of service. Hashing an enormous password is expensive, so refusing to do it is reasonable. But a refusal is a failure, and failures now return `*`.

**3. OpenSSH hashes passwords even for locked accounts (2016).** To close the timing-based username enumeration issue CVE-2016-6210, OpenSSH was changed to run the password hashing step even for accounts with no usable hash, so that valid and invalid usernames take the same time to answer. BleepingComputer describes this as the final ingredient.

Put them together. An attacker connects as an account whose shadow entry is `*` and sends a password of, say, 300 characters. OpenSSH dutifully hashes it. musl refuses because it is over 256 bytes and returns `*`. OpenSSH compares the result to the stored value, which is also `*`. They match, and the login succeeds.

The researcher's write-up gives the working range as passwords between 257 and 1024 characters. Sources differ slightly on whether the limit is counted in bytes or characters, so treat the exact boundary as approximate.

The bug does not bypass accounts that have a real password hash, per BleepingComputer. It only helps against accounts that were meant to be unreachable by password.

## Why Alpine is the worrying case

Locked accounts are normal. Key-only service users, LDAP users and root on many systems all carry a `*` or similar. What turns this from an odd quirk into a serious problem is what those accounts can do once someone is logged in.

The researcher points out that on Alpine's official AWS and Azure cloud images, the default `alpine` user has passwordless `doas`, Alpine's sudo equivalent. So the chain from "locked account" to "root" is short: log in with a long password, run `doas`, done.

I would not overstate the reach beyond that. Whether you get root depends on which account is `*`, whether it can escalate, and whether password authentication is on. But "password authentication enabled on an internet-facing sshd" is a very common default in the container and appliance world, and plenty of people never touch it.

## It was exploited within hours

The sshhole.com page itself says that, as far as anyone knows, nobody had noticed the bug. That did not last. [Help Net Security](https://www.helpnetsecurity.com/2026/11/06/openssh-sshole-cve-2026-123158-exploitation/) reports that threat intelligence firm Previdian, through founder Ryan Dewhurst, caught attacks on its sensors:

- The first observed attempt came **less than nine hours** after the CVE was published
- Previdian confirmed **root access** on a honeypot running real Alpine Linux and OpenSSH
- All eight attempts it counted came from a single IP address, and after getting in the attacker ran basic reconnaissance commands (`id`, `uname`, `hostname`) rather than anything destructive

Two caveats. This is one firm's telemetry from one sensor, so it says "exploitation is happening" rather than "here is the scale of it". And Help Net Security notes that CISA had not added the flaw to its Known Exploited Vulnerabilities catalogue at the time of writing. Previdian also warns that public proof-of-concept code on GitHub is unverified and may itself contain malware, which is worth remembering before anyone runs one to "test" their own systems.

OpenSSH developer Damien Miller was blunt about the response, according to Help Net Security: "stop reading and set PasswordAuthentication=no or disable SSH for these systems IMMEDIATELY".

## What the OpenSSH fix says

The [OpenSSH release notes](https://www.openssh.org/releasenotes.html) for 10.6p2, dated 5 November 2026, describe it as containing "a critical security workaround that affects Linux systems that use the musl libc and PAM disabled". The notes say the maintainers consider the root cause to be outside sshd, but that it is exploitable through sshd and can be avoided there, which is why the fix landed in OpenSSH.

That framing is worth pausing on. It is a fair description of the situation, and a nice illustration of why this class of bug survives. The OpenSSH side assumed `crypt()` would behave like every other implementation. The musl side assumed callers would treat `*` as a failure. Neither assumption is written down anywhere that the other project would read.

## What to do

In rough priority order:

1. **Find your musl systems.** Alpine hosts, Alpine-based container images that run sshd, OpenWrt routers, Buildroot and Yocto devices. Do not assume from the distro name.
2. **Patch.** Upgrade to OpenSSH 10.6p2 or your distribution's patched package. On Alpine, BleepingComputer gives `apk upgrade openssh`.
3. **Restart sshd.** Help Net Security stresses that installing the package does not restart the running daemon, so the old vulnerable process keeps serving connections until you do.
4. **If you cannot patch immediately,** set `PasswordAuthentication no` in the sshd configuration and restart. Key-based login keeps working.
5. **Check your logs.** Look for `Accepted password for` entries involving accounts that should never accept a password. BleepingComputer suggests `grep "Accepted password" /var/log/messages` on Alpine, and checking that the `alpine` account's entry in `/etc/shadow` still shows `*`. If you see a password login for an account that should not have one, treat it as a possible compromise.
6. **Rebuild images.** Containers and cloud images with the vulnerable package baked in need to be rebuilt and redeployed, not just patched on the running host.

## My read

This is the kind of bug I find genuinely instructive, and I want to be careful to label the following as opinion rather than reported fact.

The usual advice after a vulnerability like this is "validate return values", and that is true but a bit glib. The more useful lesson is about **in-band signalling**. A `*` in the hash field means "locked". A `*` returned from `crypt()` means "I failed". They are the same string carrying two different meanings, and the bug lives entirely in that overlap. Whenever an error value and a legitimate value can be the same thing, you have built a trap, and it only springs when someone finds an input that triggers the error path on purpose.

It is also a reminder that hardening can be the thing that exposes a flaw. The 2016 enumeration fix was a correct and worthwhile security improvement. It is simply the change that put the `*` comparison in the path of attacker-controlled input.

The practical takeaway is dull and effective: turn off password authentication on anything internet-facing, patch, restart, and stop assuming a locked account is a locked door.

## Sources

- [sshhole.com - original research and demo](https://sshhole.com/)
- [OpenSSH release notes](https://www.openssh.org/releasenotes.html)
- [Help Net Security - OpenSSH flaw exploited in the wild just hours after disclosure (CVE-2026-123158)](https://www.helpnetsecurity.com/2026/11/06/openssh-sshole-cve-2026-123158-exploitation/)
- [BleepingComputer - OpenSSH flaw lets attackers log into password-disabled Linux accounts](https://www.bleepingcomputer.com/news/security/openssh-flaw-lets-attackers-log-into-password-disabled-linux-accounts/)

## Related Reading

- [Understanding Types of Cyber Attacks: A DevOps Guide](/devops/cyber-attack-types/)
- [Threat Modeling for Engineers: Finding the Flaws Before Attackers Do](/security/threat-modeling-for-engineers/)
