# AVZON — "A New Horizon, Engineered" · expanded production prompt

## Style block (from frame.md, verbatim)

void `#050608` · graphite `#0D0F14` · steel `#1C2029` · hairline `#2E3440` · mist `#8B919D`
· porcelain `#F2F0EB` · ion `#4B5FFF` (the one accent) · ion-tint `#9AA6FF` (accent text).
Display: **Archivo** at 125% width, weights 150–200 (precision) and 850–900 (force); the
width axis animates. Instrument: **Geist Mono** 20–24px, uppercase, tracked 0.14em.
Wordmark: a custom SVG with five square modules, Λ V Z O N.

## Rhythm declaration

120 BPM, with a 0.5 s beat and bars on even seconds.
`slow-build (ignite) → REVEAL (object) → PUNCH·PUNCH·PUNCH (triad) → VACUUM → IMPACT/ASSEMBLE → breathe → sign-off`

| # | Scene        | Window        | Energy       | Out-transition                         |
| - | ------------ | ------------- | ------------ | -------------------------------------- |
| 1 | Ignition     | 0.00 – 2.50   | low → rising | solar overexposure burn @2.50          |
| 2 | Halo         | 2.50 – 5.50   | medium       | zoom-through the ring's bore @5.50      |
| 3 | Velocity     | 5.50 – 8.50   | high         | hard cut on the beat @8.50              |
| 4 | Convergence  | 8.50 – 10.00  | peak → vacuum| impact white flash @10.00               |
| 5 | Lockup       | 10.00 – 15.00 | resolve      | final fade to void 14.40 – 15.00        |

## Global rules

- Persistent host layers: film grain (soft-light, seeded 512² tile, stepped at 24 Hz),
  a radial vignette, and an instrument HUD (corner brackets, sequence label, timecode,
  and a progress rail) from 0.25 to 9.95 s. The HUD is hidden during the lockup.
- Canvas layers are driven by a **property-setter driver** tweened linearly across the
  scene, never by `onUpdate`, so seeks always repaint.
- SVG strokes draw via the `stroke-dashoffset` **attribute**.
- Parallax: the background glow moves at about 0.4× the camera move, and the HUD is fixed.
- Primary transitions are light and zoom. The accent transition is the impact flash at
  the hero reveal. No exit animations except in the final scene.

## Scene 1 — IGNITION (0.00–2.50)

**Concept.** Darkness, then first light breaking over the curved limb of an unseen
world, like sunrise seen from orbit. It's vast and quiet, with the feeling that
something is about to arrive.
**Mood.** 2001's monolith dawn; Apple event teasers; Interstellar's quiet scale.
**Depth.** BG: void, a sparse seeded dust field (48 points at 1–2px, 15–35% alpha,
slow twinkle), and an ion atmosphere band hugging the limb. MG: the planet limb, a disc
of r≈3000px centered below the frame with its top at y≈760. It has a razor porcelain
rim, brightest at center and fading toward the edges. The sun point sits on the limb
at x=960. FG: the HUD.
**Choreography.**
- 0.20–1.40: the rim light SPREADS from center to both edges (arc draw, `power2.out`).
- 0.30–0.80: the sun core IGNITES (core radius 0→1, bloom 0→1, `expo.out`).
- 0.35–1.35: the anamorphic streak EXTENDS (half-length 0 → 780px, `expo.out`), with
  quarter-res buffer tent streaks tinted ion.
- 0.90–2.00: the atmosphere band BREATHES up (0 → 1).
- Camera: the world DRIFTS up and pushes in (scale 1.00→1.07, y 0→-26px, `sine.inOut`).
- 2.05–2.50: the sun SWELLS (core ×3, bloom ×2.4) into the transition burn.
**Transition out.** An overexposure burn: the flash overlay ramps 2.28→2.50 (`power2.in`),
the scene swaps at the peak, and the wash decays 2.50→2.85 (`power2.out`).
**SFX.** Sub drone swell 0→2.5; a crystalline tick @0.30; an air shimmer 1.4→2.5;
a deep boom + noise burst @2.50.

## Scene 2 — HALO (2.50–5.50)

**Concept.** Out of the light, the object: a perfect ring machined from dark metal,
floating and turning slowly while studio light rakes across its engraved bezel.
Hairline engineering drawings measure it. This is precision you can see.
**Mood.** Product-film macro (Apple Watch bezel, Leica lens barrels); technical drawing.
**Depth.** BG: void, an ion backlight glow behind the ring that breathes, and the ghost
title **PRECISION** (Archivo 125%/150, ~210px, porcelain at 16%) behind the ring, so the
ring occludes it. MG: the Halo, a canvas ring (outer R 430, bore 350, wall 64). Tilt
eases 68°→58°, spin 0→38°, and roll −3°→2°. It has a brushed top face (two soft light
lobes), 120 engraved ticks (every 10th long), a knurled outer wall, and chamfer
highlights. FG: an SVG dashed construction ellipse, center crosshair, a Ø dimension
line with arrow ticks and label `Ø 1.000`, a `360°` arc callout, `AXIS · Z`, and four
registration crosses.
**Choreography.**
- 2.50–3.20: the ring's exposure RISES out of the flash (lighting 0.25→1).
- 2.60–3.90: PRECISION letter-spacing COLLAPSES 0.42em→0.02em (`power4.out`), opacity 0→0.16.
- 2.90–3.70: the construction ellipse DRAWS (`power2.out`); crosshairs EXTEND from center.
- 3.35–3.85: the Ø dimension line DRAWS, then the label TYPES on (seeded decode).
- 3.70: the `360°` and `AXIS · Z` callouts SNAP in (opacity steps + 8px slide).
- 4.00–4.85: a specular sweep ORBITS the rim (one pass), and the backlight PULSES.
- 4.85–5.15: hold (the ring keeps turning; the ticks visibly travel).
- 5.15–5.50: the camera PUSHES into the bore (scale 1→2.6 around the ring center,
  blur 0→14px, `power3.in`).
**Transition out.** A zoom-through: velocity-matched with scene 3's entry (scale 0.55→1,
blur 14→0, 0.45 s `expo.out`).
**SFX.** A soft kick pulse starts @3.0 (every beat); a metallic ping @4.00; a whoosh
5.2→5.6.

## Scene 3 — VELOCITY (5.50–8.50)

**Concept.** Through the bore and into pure momentum: a tunnel of engraved rings
streams past like the optics of a machine, and three words land like heartbeats.
**Mood.** Precision-optics hyperspace; Nike speed graphics; Swiss kinetic type.
**Depth.** BG: void and the ring tunnel (canvas), with 26 rings on a z-loop and a
perspective vanishing point at (960, 540). Each ring is a hairline circle, some
graduated with ticks, with a porcelain specular arc at the upper-left and every 5th
ring in ion. Rings fade with distance (fog) and leave 3-step motion trails. Speed
ramps up and kicks on each word. MG: kinetic words. FG: the HUD's beat counter and
horizontal speed hairlines on each hit.
**Choreography.** One beat array: `HITS = [6.00, 6.75, 7.50]`.
- 6.00 **FORM.**: SLAMS (scale 1.55→1, blur 18→0, `power4.out`, 0.42 s), 900 weight.
- 6.75 **FUNCTION.**: SNAPS in from the right (x +760→0, directional SVG blur 40→0,
  `expo.out`, 0.34 s). FORM hard-cuts out on the same frame.
- 7.50 **FUTURE.**: RISES and EXPANDS (y 70→0, wdth 62%→125%, wght 250→900, 0.62 s
  `expo.out`). FUNCTION hard-cuts out.
- 8.05–8.50: FUTURE's tracking OPENS (0→0.16em) and it SCALES toward camera
  (1→1.18) as the tunnel hits max speed. Hard cut @8.50.
**SFX.** Kick every beat; big layered hits on 6.00 / 6.75 / 7.50 (rising pitch); a
riser starts 8.0.

## Scene 4 — CONVERGENCE (8.50–10.00)

**Concept.** Everything that moved is pulled back into a single point. The five
primitives of the mark tumble inward like debris into a singularity, a countdown ticks,
and then silence.
**Depth.** BG: void, plus 700 seeded particles spiraling inward on log-spiral paths
(canvas, `power2.in` time-warp) with short trails. MG: five outlined glyph primitives
(Λ V Z O N) starting scattered at depth (rotateX/Y ±70°, translateZ −600…400) and
converging to the center while shrinking. The small ring spins up at the center. FG:
the HUD countdown `T–01.50 → T–00.00` in ion-tint.
**Choreography.**
- 8.50–9.60: particles and glyphs CONVERGE (`power2.in`), and the ring SPINS up.
- 9.60–9.85: everything COLLAPSES to a pinpoint (scale→0); the frame goes near-black
  (vacuum).
- 9.85–10.00: the pinpoint INTENSIFIES, then the flash at 10.00.
**SFX.** The riser climbs to 9.85, then a hard cut to silence (the suck), then the impact @10.00.

## Scene 5 — LOCKUP (10.00–15.00)

**Concept.** From the flash, the mark builds itself with mechanical certainty on an
engineering grid. It enters scrambled as **V Λ N ○ Z**: the chevrons counter-flip,
the strokes counter-rotate like meshing gears, and the ring (the Halo) seats as the
axle, so the name decodes to **Λ V Z O N** through pure geometry. Then it rests on
the returning horizon line, lit like a product on a plinth.
**Depth.** BG: void, a porcelain/ion bloom behind the mark (ambient-glow-bloom), and
the horizon baseline that returns from scene 1. MG: the SVG wordmark (cap height 176px,
porcelain) and the construction grid (five square modules, corner ticks, circle and
diagonal guides). FG: the tagline in Archivo 125%/300 at 30px, tracked 0.42em, and the
sign-off in Geist Mono with a pulsing ion dot.
**Choreography.**
- 10.00: the impact flash (wash peak), decaying by 10.35.
- 10.02–10.40: grid modules DRAW from the center outward (stagger 0.05).
- 10.06–10.55: the O ring LANDS (scale 2.4→1, spin decelerates, `power4.out`) with a
  rim flare and a lock tick.
- 10.22–10.55: modules 1–2 DROP in as **V Λ** (y −140→0, streak blur, `power4.out`,
  stagger 0.06).
- 10.30–10.62: modules 3 and 5 RISE in as **N** and **Z** (y +140→0, `power4.out`).
- 10.60–11.05: module 1 FLIPS V→Λ and module 2 flips Λ→V (rotationX, `power3.inOut`),
  with a specular flash at edge-on.
- 10.66–11.12: module 3 ROTATES N→Z (−90°→0°) and module 5 rotates Z→N (+90°→0°),
  counter-rotating (`back.out(1.15)`).
- 11.05–11.85: a specular glint SWEEPS across the mark (L→R, `power2.inOut`); the
  horizon line EXTENDS from center to 1800px.
- 11.25–11.75: the grid FADES to 0.
- 11.60–12.40: the tagline WIPES in (clip-path L→R) while its tracking settles
  0.62em→0.42em.
- 12.40–13.20: breathe; the bloom breathes and the lockup pushes 1.0→1.025 (whole scene).
- 13.20: `COMING SOON` TYPES on (mono); the ion dot PULSES twice.
- 14.20: the ring WINKS (a rim glint travels once around the O).
- 14.40–15.00: everything FADES to void (`power2.in`).
**SFX.** A massive impact @10.00; a ring-lock ping @10.10; drops/whooshes @10.22;
mechanical clicks @10.62, @10.70, @11.05; a pad chord swell from 10.0; a glint shimmer
@11.05; a soft ping @13.20; a shimmer @14.20; the tail ends by 15.0.

## Recurring motifs

The ring (limb disc → Halo → tunnel rings → axle → O) · the horizon line (limb →
baseline) · ion backlight · mono instrument readouts · light that travels (rim spread,
orbiting specular, glint sweep, final wink).

## Negative prompt

No neon cyan, no purple→blue gradients, no gradient-filled text, no rounded display
faces, no starfield warp clichés, no lens-flare polygons, no bouncy or elastic easing,
no fake specs or claims, no ®/™, and no centered-and-floating web layouts in the HUD.
