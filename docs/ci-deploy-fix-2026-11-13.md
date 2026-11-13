# CI deploy fix (13 November 2026)

The GitHub Actions workflow (`.github/workflows/deploy.yml`) was failing, so pushes to `main` were not deploying. Three separate problems had to be fixed in turn.

## Problem 1: build failed on the `x` shortcode

- **Error:** `failed to extract shortcode: template for shortcode "x" not found` in `content/ai/tweets/auto-gpt.md`.
- **Cause:** The workflow pinned `HUGO_VERSION: "0.140.2"`. The built-in `x` shortcode (tweet embeds) arrived in Hugo 0.141, and PaperMod needs at least 0.146.0. Local Hugo was 0.159.2, so builds worked locally.
- **Fix:** Bump `HUGO_VERSION` to `0.159.2` (commit `e9c58560f`).

## Problem 2: deploy could not reach the server

- **Error:** `ssh: connect to host jamesm.blog port 22: Network is unreachable`, after hanging about 4.5 minutes.
- **Cause:** `jamesm.blog` is proxied by Cloudflare, which does not pass SSH. Locally this works only because `~/.ssh/config` maps `jamesm.blog` to the origin IP. The CI runner has no such mapping.
- **Fix** (commit `e1e16745f`):
  - rsync now targets the `DEPLOY_HOST` repo secret, which holds the origin IP (kept out of this public repo).
  - `-o HostKeyAlias=jamesm.blog` so host-key checking still uses the `jamesm.blog` name.
  - `-o ConnectTimeout=20` so a blocked connection fails fast.

## Problem 3: missing secrets

- **Error:** `No ED25519 host key is known for jamesm.blog and you have requested strict checking.`
- **Cause:** Neither `DEPLOY_KNOWN_HOSTS` nor `DEPLOY_SSH_KEY` had been set on the repo (or the `production` environment).
- **Fix:**
  1. Scan the server key, check it matches the local `~/.ssh/known_hosts` entry, and set the secret:
     ```
     ssh-keyscan -t ed25519 <ORIGIN_IP> | sed 's/^<ORIGIN_IP>/jamesm.blog/' | gh secret set DEPLOY_KNOWN_HOSTS --repo jmydde/jamesm.blog
     ```
  2. Generate a dedicated deploy key (not the personal key), store the private half as `DEPLOY_SSH_KEY`, and delete the local private key:
     ```
     ssh-keygen -t ed25519 -N "" -C "github-actions-deploy jamesm.blog" -f k
     gh secret set DEPLOY_SSH_KEY --repo jmydde/jamesm.blog < k && rm k
     ```
  3. Authorize the public half on the server (run by hand, since it changes root login access):
     ```
     ssh jamesm.blog "echo '<contents of k.pub>' >> ~/.ssh/authorized_keys"
     ```
  4. Rerun the failed job: `gh run rerun <run-id> --failed`.

## Result

Run `43514092290` passed: build in 17s, deploy in 8s. Pushes to `main` now deploy automatically.

## Notes for the future

- **Rotating or revoking:** the deploy key's public line ends with `github-actions-deploy jamesm.blog`. Delete that line from the server's `~/.ssh/authorized_keys` to revoke it, then regenerate and reset `DEPLOY_SSH_KEY`.
- **If the origin IP changes** (see the comment in `~/.ssh/config`): update the `DEPLOY_HOST` secret, and refresh `DEPLOY_KNOWN_HOSTS` if the host key changed too.
- **Hugo version:** keep `HUGO_VERSION` in the workflow at or above the local version and PaperMod's minimum.
- **Pre-deploy checks:** `deploy.sh` runs `validate-tags.py` and `link-audit.py` before rsync. The workflow does not, so run them locally first.
