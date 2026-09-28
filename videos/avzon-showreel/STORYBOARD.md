---
format: 1920x1080
duration: 15s
message: "AVZON is a high-end, modern tech brand: precise, powerful, and about to launch."
arc: Ignite → Object → Velocity → Convergence → Lockup
audience: portfolio visitors and prospective clients judging premium motion-design craft
mode: autonomous
fps: 60
tempo: 120bpm
music: "bespoke synthesized score: sub drone, beat-locked pulse, triad hits, riser, vacuum, impact, pad resolve"
---

## Frame 1 — Ignition

- scene: First light breaks over a curved horizon; an anamorphic streak spreads along the limb
- duration: 2.5s
- poster: 1.6s
- transition_in: cut
- status: animated
- src: compositions/s1-ignition.html
- blueprint: none. Composed from rules
- rules: ambient-glow-bloom, svg-path-draw (arc spread via canvas equivalent), multi-phase-camera (slow push + drift)
- transition_out: overexposure burn @2.50 (transitions/css-light.md → Overexposure Burn)

Wordless. Darkness, then a sun point ignites on the limb of an unseen world. The rim
light spreads outward and the atmosphere glows ion. The HUD brackets draw on in the
corners. The sun swells into white at 2.5 s.

## Frame 2 — Halo

- scene: A precision-machined ring turns in raking light while hairline engineering drawings measure it
- duration: 3s
- poster: 1.6s
- transition_in: overexposure burn
- status: animated
- src: compositions/s2-halo.html
- blueprint: logo-assemble-lockup (Product_Intro orbit-sting shape: a fixed hero object, a system of guides assembling around it, one camera move)
- rules: svg-path-draw, ambient-glow-bloom, multi-phase-camera (push-through), gsap-effects (letter-spacing collapse)
- transition_out: zoom-through the bore @5.50 (transitions/css-scale.md → Zoom through, velocity-matched)

The product object, never named. The ghost title PRECISION collapses its tracking
behind the ring. A Ø dimension line and callouts type on. A specular sweep orbits the
rim on the 4.0 s downbeat, then the camera dives into the bore.

## Frame 3 — Velocity

- scene: A tunnel of engraved rings streams past as FORM. FUNCTION. FUTURE. land on the beat
- duration: 3s
- poster: 1.75s
- transition_in: zoom-through
- status: animated
- src: compositions/s3-velocity.html
- blueprint: kinetic-type-beats (sub-shape B, multi-beat statement build; Benefits staccato)
- rules: kinetic-beat-slam (one HITS array, distinct entrances), motion-blur-streak (FUNCTION side-snap), 3d-camera-flight (tunnel perspective, canvas)
- transition_out: hard cut @8.50

Momentum. There are three words, each with its own physical character. FORM slams in
depth, FUNCTION whips in laterally with a directional smear, and FUTURE rises while its
width axis expands from condensed to extended. The tunnel kicks on every hit.

## Frame 4 — Convergence

- scene: Particles and the five glyph primitives implode into a single point; the countdown hits zero
- duration: 1.5s
- poster: 0.8s
- transition_in: cut
- status: animated
- src: compositions/s4-converge.html
- blueprint: logo-assemble-lockup (CTA text-clear bloom: the stage clears to a vacuum before the mark forms)
- rules: depth-scatter-assemble (radial / depth-cloud run inward), particle-burst (deterministic pool, closed-form paths), discrete-text-sequence (countdown)
- transition_out: impact flash @10.00 (editorial-flash-overlay, adapted)

The inhale before the reveal. Everything is pulled into the center and the frame goes
nearly black for a beat of vacuum.

## Frame 5 — Lockup

- scene: The wordmark decodes V Λ N ○ Z → Λ V Z O N by flips and counter-rotations, then rests on the horizon
- duration: 5s
- poster: 3.4s
- transition_in: impact flash
- status: animated
- src: compositions/s5-lockup.html
- blueprint: logo-assemble-lockup (Product_Intro parts-assembly + Brand_Outro settled-reveal)
- rules: svg-path-draw (construction grid), spring-pop-entrance (ring seat), hacker-flip-3d (rotateX flip axis), motion-blur-streak (drop-ins), ambient-glow-bloom, css-marker-patterns (horizon underline sweep)
- transition_out: final fade to void 14.40–15.00

The payoff. The mark enters scrambled and resolves through its own geometry: Λ is a
flipped V, and Z is a rotated N. A glint sweeps across it, the horizon returns as its
baseline, and the tagline ENGINEERED FOR WHAT'S NEXT wipes in. COMING SOON follows,
then a final rim wink and a fade.
