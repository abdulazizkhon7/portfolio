---
workflow: general-video
flow: automation
storyboard: no
message: "AVZON is a high-end, modern tech brand: precise, powerful, and about to launch."
destination: website
aspect: 1920x1080
language: en
audience: portfolio visitors and prospective clients judging premium motion-design craft
length: 15s
angle: product-launch teaser
narration: no
---

## Intent

A premium 15-second motion graphics showreel for AVZON that instantly communicates
a high-end, modern tech brand. In the user's words: "Make it feel like a world-class
product launch teaser created by a top-tier motion designer." "Deliver a polished,
production-quality result that looks portfolio-worthy and feels…" (the request was
cut off at this point).

Concept (chosen internally; autonomous run): **"A new horizon, engineered."** Light
rises over a curved horizon, becomes a precision-machined ring (the product object,
never named), accelerates through the brand's own chevrons, and collapses into a
wordmark that assembles itself from its own geometry. Λ is a flipped V, and Z is a
rotated N. Typical direction left behind: a stock "glitch + neon HUD" tech montage.

## Assets

- none supplied (no logo, product imagery, copy, palette, or music). The AVZON
  wordmark is drawn from scratch for this piece as a geometric SVG.

## Customizations

- Bespoke sound design: a synthesized, edit-locked score (120 BPM, 0.5 s beat grid)
  layered with the bundled Pixabay-licensed SFX library (impacts, whooshes, riser, glints).
- Copy: "PRECISION" (ghost title), "FORM. FUNCTION. FUTURE." (kinetic triad),
  tagline "ENGINEERED FOR WHAT'S NEXT", sign-off "COMING SOON". No product claims,
  no specs, no ®/™ marks.

## Notes

- The request's "Specifications" and "Creative Direction" sections arrived empty, and
  its final sentence was truncated. Defaults below were chosen and must be surfaced
  in the handoff so the user can correct them:
  16:9 1920×1080 (portfolio/website), 60 fps delivery, 15.0 s exactly, English,
  dark premium palette, music + SFX.
- Environment: `cdn.jsdelivr.net` is denied by the network policy, so GSAP 3.14.2 is
  vendored from npm into `assets/vendor/`. Chrome's WebGL is unavailable (software
  mode), so there are no shader transitions or Three.js. Everything is Canvas 2D, SVG,
  and CSS.
- Avoid: cyan-on-dark and purple→blue gradients (the portfolio site itself is cyan;
  AVZON is a separate brand), gradient-filled text, rounded "web3" display faces,
  bouncy/elastic easing, starfield clichés, fake specs.
- Orange is deliberately avoided: next to a name like "AVZON" it would read as Amazon.
