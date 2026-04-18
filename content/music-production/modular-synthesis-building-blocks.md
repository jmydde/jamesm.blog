---
title: Introduction to Modular Synthesis - The Building Blocks
date: 2026-04-18T09:00:00+01:00
draft: false
tags: ["music-production", "synthesis", "modular", "eurorack", "sound-design"]
description: "A practical guide to understanding modular synthesis fundamentals. Learn what oscillators, envelopes, filters, and LFOs actually do, and how they connect to create sound."
---

Modular synthesis can feel overwhelming at first. There are dozens of modules, hundreds of cables, and infinite ways to patch them together. But underneath all that complexity lies a simple truth: modular synthesis is about understanding how audio flows from one place to another, and learning to shape that signal at every step.

If you've ever felt lost looking at a Eurorack case, this post is for you. We're going to break modular synthesis down to its essential building blocks - the modules that do the heavy lifting in almost every patch.

## The Signal Flow: Where Everything Starts

Before we talk about individual modules, understand this: in modular synthesis, everything is about signal flow. You start with a signal generator (usually an oscillator), shape it with processors (filters, amplifiers), modulate it with controllers (LFOs, envelopes), and send it somewhere useful (an output, or into another module).

Think of it like plumbing. You have a water source (oscillator), pipes connecting them (cables), valves that control flow (mixers, VCAs), and outlets where the water goes (speakers).

## The Oscillator: Your Raw Material

An oscillator generates a repeating waveform at a specific frequency. This is your sound source.

The four basic waveforms are:

**Sine wave** - Pure, smooth, no harmonics. Use when you want something warm and simple. A sine wave at 440 Hz is an A note. The sine wave teaches you something important: the oscillator doesn't know what note it's playing. Frequency is just a number. If you send 440 Hz, you hear A. If you send 220 Hz, you hear the A an octave lower. The oscillator is indifferent.

**Square wave** - Bright, hollow, full of odd harmonics. Think of it as a digital, synth-like sound. Square waves are hostile. They cut through a mix.

**Sawtooth wave** - Rich, dense, full of both even and odd harmonics. The most aggressive and buzzy of the basic waveforms. If you're building a lead sound, the sawtooth is often your starting point.

**Triangle wave** - Somewhere between sine and square. Smoother than square, but with more character than sine. Less harmonically rich than sawtooth.

You can blend between these waveforms on many oscillators. Most patches won't start with pure waves - they'll use a blend to get something more interesting than any single wave alone.

## The Filter: The Sculptor's Tool

A filter removes or attenuates frequencies. This is where modular synthesis gets interesting.

The **low-pass filter** is the most important filter in synthesis. It lets low frequencies through and removes high frequencies. Sweep a low-pass filter across a sawtooth wave and you've heard the sound of synthesis. As you close the filter (lower the cutoff frequency), the sound gets rounder, warmer, less aggressive. This single interaction - cutoff frequency - is the foundation of classic analog synthesis.

Other filters:

**High-pass filter** - Removes low frequencies, lets highs through. Use when you want to strip out the bottom and get a thin, nasal quality.

**Band-pass filter** - Lets a specific range of frequencies through, removes everything else. Creates hollow, focused sounds.

**Notch filter** - The opposite. Removes a specific frequency range, lets everything else through. Useful for cleaning up problem frequencies.

Filters have another crucial parameter: **resonance** (sometimes called Q). At low resonance, the filter just smoothly attenuates. At high resonance, it emphasizes frequencies right at the cutoff point, creating a peak. Push resonance too far and the filter self-oscillates, creating its own tone independent of the input. This is a feature, not a bug. A resonant filter self-oscillating becomes an oscillator.

## The Envelope: The Shape of Your Sound

An envelope describes how a sound changes over time. It starts somewhere, goes somewhere, and ends somewhere.

The **ADSR envelope** is the standard:

**Attack** - How long does it take to reach full volume after you press a key? A slow attack (500ms) makes the sound swell in. A fast attack (1ms) makes it punchy.

**Decay** - After reaching peak, how long until you drop to the sustain level? A fast decay and low sustain give you a pluck. A slow decay makes the sound ring out.

**Sustain** - What volume level do you hold while the key is pressed? This is not time - it's a level. It's the only non-time parameter.

**Release** - After you release the key, how long until silence? A fast release (50ms) makes the sound cut off abruptly. A slow release (2s) lets it ring out like a bell.

On a piano, the ADSR is built into the mechanics: when you hit a key, the hammer attacks fast, the sound decays slightly, sustains while the key is held, and releases when you release the key.

In a synthesizer, you can shape this any way you want. A short attack, no decay, low sustain, fast release makes a click or pluck. A slow attack, long decay, no sustain (0), slow release makes a swelling, ambient sound.

The envelope is one of the most powerful tools in synthesis. Two patches with identical oscillators and filters but different envelopes will sound completely different.

## The LFO: Modulation in Motion

An LFO (Low Frequency Oscillator) is an oscillator that runs very slowly - typically between 0.1 Hz and 20 Hz. Instead of being turned into sound, it modulates (changes) another parameter.

The most common use: modulate the filter cutoff with an LFO. Now your filter sweeps automatically. This is how you get the "wow wow wow" sound of a classic Moog pad, or the wobble of a vintage Juno chorus effect.

LFO modulation can go to:
- **Filter cutoff** - Creates a rhythmic filtering effect
- **Oscillator pitch** - Creates pitch vibrato or wobble
- **Amplitude (volume)** - Creates tremolo (volume modulation)
- **Pan** - Moves the sound left and right in stereo

The LFO typically has the same waveform options as an oscillator (sine, square, sawtooth, triangle), plus rate (how fast it oscillates) and depth (how much it modulates the target).

## The VCA: The Amplifier You Control

A VCA (Voltage Controlled Amplifier) is an amplifier whose gain is controlled by a voltage. In practice, this is how you control volume with an envelope or an LFO.

When your envelope triggers, it sends out a control voltage. That voltage goes into a VCA's modulation input, which controls how loud the signal is. As the envelope rises, the VCA opens and the signal gets louder. When the envelope falls, the VCA closes and the signal gets quieter.

This is fundamental: in modular synthesis, everything that changes a sound is controlled by a voltage. An envelope sends a voltage to a VCA, which controls volume. An LFO sends a voltage to a filter, which controls cutoff. An external sequencer sends pitch voltage to an oscillator, which changes what note plays.

## The Mixer: Combining Signals

A mixer takes multiple audio signals and combines them. You might mix:
- Multiple oscillators together (for richer tones)
- Multiple envelopes (to blend different modulation sources)
- Dry and wet signals from an effect

A mixer also lets you control the level of each input independently, so you can blend oscillators in the ratio you want.

## Putting It Together: A Basic Patch

Here's a simple, complete patch that demonstrates these concepts:

1. **Oscillator** generates a sawtooth wave
2. **Filter** (low-pass, with some resonance) processes the sawtooth
3. **ADSR envelope** generates a control signal
4. **VCA** takes the envelope and controls the amplitude of the filtered signal
5. **LFO** modulates the filter cutoff slowly, creating movement
6. Your modulation input (typically a keyboard) controls the oscillator pitch and triggers the envelope

When you press a key:
- The keyboard sends pitch voltage to the oscillator (changes what note)
- The keyboard sends a trigger to the envelope
- The envelope rises (attack), falls to sustain level (decay), holds (sustain)
- The VCA opens and closes with the envelope, controlling volume
- The LFO slowly sweeps the filter cutoff back and forth
- You hear a warm, slowly morphing pad sound

This is 90% of what you need to know to start patching. Most synthesizer patches are variations on this theme.

## Why Modular Feels Hard (And Why That's Okay)

Modular synthesis is hard because:
1. There are infinite possibilities, so you have to make every decision
2. Nothing is preset - if you want it to work, you have to understand why
3. One mispatched cable can produce nothing, noise, or something expensive-sounding but uncontrollable

This is also why it's powerful. Once you understand the signal flow - oscillator to filter to amplifier - and the modulation sources - envelope, LFO, keyboard - you can build sounds that would take hours to program on a traditional synthesizer.

## Next Steps

Start small. Learn one oscillator, one filter, one envelope, one VCA. Understand how they connect and what each parameter does. Patch them together and move each knob one at a time, so you understand what it controls.

Then add an LFO. Then add another oscillator. Then add a mixer so you can blend them.

The building blocks are simple. The combinations are infinite.

---

## Resources

- [Eurorack Fundamentals: Format, Power, and Signal Flow](https://jamesm.blog/music-production/eurorack-fundamentals) - If you're planning to buy modules, start here.
- [Mutable Instruments](https://mutable-instruments.net/) - High-quality, documented open-source modules that teach you what each component does.
- [VCV Rack](https://vcvrack.com/) - Free software modular synth. A perfect learning tool before you buy hardware.
- [Patch Me In](https://www.patchmein.com/) - Community patches and learning resources.

