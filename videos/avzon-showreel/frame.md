---
name: AVZON / Horizon
concept: "A new horizon, engineered. Light is the protagonist; geometry is the proof."
colors:
  void: "#050608"        # background, every scene (cool-tinted near-black, never #000)
  graphite: "#0D0F14"    # raised surfaces, ring body shadow side
  steel: "#1C2029"       # structural fills
  hairline: "#2E3440"    # construction lines, grids, rules
  mist: "#8B919D"        # secondary text, HUD labels (6.4:1 on void)
  porcelain: "#F2F0EB"   # primary type, light cores, the wordmark
  ion: "#4B5FFF"         # the ONE accent hue: backlight, atmosphere, glows, rules (non-text or ≥48px)
  ion-tint: "#9AA6FF"    # accent for small text (8.7:1 on void)
typography:
  display:
    fontFamily: Archivo          # variable: wdth 62–125, wght 100–900 (embedded woff2)
    fontStretch: 125%
    weights: [150, 200, 850, 900]
    letterSpacing: -0.02em
    textTransform: uppercase
  instrument:
    fontFamily: Geist Mono       # variable: wght 100–900 (embedded woff2)
    fontSize: 20px
    fontWeight: 450
    letterSpacing: 0.14em
    textTransform: uppercase
  wordmark: "custom SVG — five square modules: Λ V Z O N (Λ = V flipped, Z = N rotated 90°)"
rounded:
  none: 0px
spacing:
  edge: 72px              # HUD / edge-anchor inset
  module-gap: 0.26        # wordmark gap, as a fraction of cap height
motion:
  tempo: 120bpm           # beat = 0.5 s; bars on even seconds
  energy: controlled-high
  easing:
    entry: "expo.out"
    exit: "power3.in"
    mechanical: "power3.inOut"
    ambient: "sine.inOut"
  duration:
    snap: 0.28
    entrance: 0.5
    cinematic: 1.2
  atmosphere: [film-grain, ion-backlight, hairline-construction, mono-instrument-hud]
---

## Overview

AVZON is a premium technology brand revealed through a teaser. Its look is **restraint
under pressure**. The palette is near-black and porcelain, with one electric ion-blue
accent that behaves like light, not paint. Every frame is lit, not colored: glows have
physical falloff, highlights move across surfaces, and nothing is flat.

## The frame

- Background is always `void`, with a film grain overlay (soft-light) to kill banding
  in dark gradients. No full-screen linear gradients: glows are radial and localized.
- The accent `ion` appears as backlight, atmosphere, and thin rules. Small text in the
  accent uses `ion-tint`. Accent coverage is at most about 15% of any frame.
- Porcelain is the only "hot" value. Pure white is reserved for light cores and flashes.

## Typography

- **Archivo** at 125% width is the one expressive family. It lives at the extremes:
  150–200 weight is the voice of precision (ghost titles, tagline), and 850–900 is the
  voice of force (kinetic words). The width axis itself animates (62% → 125%) on "FUTURE."
- **Geist Mono** is the instrument voice: HUD, callouts, timecode, sign-off. It is
  always uppercase and tracked, at 20–24px, and never used for statements.
- The wordmark is **not a font**. It is five geometric glyphs drawn on a square module
  grid, with flat terminals and a monoline stroke of 0.18 × cap height.

## Composition rules

- HUD elements anchor to the edges (72px inset). Hero content owns the center; the HUD
  owns the corners.
- Every scene has a background treatment (glow, horizon, tunnel, or grid), midground
  content, and foreground instrument detail.
- Two focal points minimum: the hero plus one instrument readout or glint.

## Motion

- Entrances use `expo.out`, exits use `power3.in`, and mechanical moves (flips,
  rotations, locks) use `power3.inOut` or `back.out(1.2)` at most. There is no elastic
  or bounce.
- Every decorative element breathes (glow), drifts (camera), or ticks (instrument).
- Cuts land on the 0.5 s beat grid. Word hits run a syncopated 0.75 s pulse
  (6.00 / 6.75 / 7.50).

## Do's and Don'ts

- Do let light travel: specular sweeps, rim flares, and horizon lines are the brand's
  signature.
- Do reuse the brand's own geometry (ring, chevron, rotated stroke) as the motion system.
- Don't use gradient-filled text, neon cyan, purple→blue washes, rounded display faces,
  starfields, lens-flare polygons, or fake specifications.
- Don't use ® or ™, and don't make product claims. The product stays a mystery; that is
  the teaser.
