# AVZON — Showreel (15 s)

A 15-second motion-graphics teaser for **AVZON**, built as a
[HyperFrames](https://hyperframes.heygen.com) composition (HTML → video).

**Deliverable:** `renders/avzon-showreel.mp4`, 1920×1080 at 60 fps, exactly 15.000 s.
It is H.264 High@4.2 at about 13 Mbps (24 MB) with AAC 48 kHz stereo audio mastered to
about −14 LUFS. The file is web-ready (`+faststart`). `renders/avzon-showreel-poster.jpg`
is the lockup frame for a `<video poster>`, and `renders/avzon-showreel-contact-sheet.jpg`
has one frame per scene.

The web file is encoded from a 30 Mbps delivery master
(`renders/avzon-showreel-master.mp4`, about 54 MB). The master is not committed:
`npm run render && npm run encode:web` rebuilds both.

## Concept: "A new horizon, engineered"

| Time        | Scene       | What happens                                                                                                                     |
| ----------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 0.0 – 2.5   | Ignition    | First light breaks over a curved horizon; an anamorphic streak spreads along the limb and burns to white.                        |
| 2.5 – 5.5   | Halo        | A precision-machined ring turns in raking light, measured by hairline engineering drawings, then the camera dives into its bore. |
| 5.5 – 8.5   | Velocity    | A tunnel of engraved rings; **FORM. FUNCTION. FUTURE.** land on a syncopated 0.75 s pulse, each with its own physics.            |
| 8.5 – 10.0  | Convergence | Particles and the mark's five primitives implode into a point; a beat of true silence.                                           |
| 10.0 – 15.0 | Lockup      | Impact. The wordmark enters scrambled as `V Λ N ○ Z` and decodes to **ΛVZON** by counter-flips and counter-rotations.            |

The wordmark is drawn from scratch on a square module (`tools/wordmark.py`). **Λ is a
flipped V** and **Z is N rotated 90°**, and the lockup animation is built on that
geometry.

## Project layout

```
index.html              thin orchestrator: scene slots, fx slots, score track, zoom-through
compositions/           s1…s5 scenes + fx-hud (instrument HUD), fx-flash (light rig), fx-grain
index.motion.json       motion assertions verified by `hyperframes check`
frame.md                design spec (palette, type, motion rules)
BRIEF.md, STORYBOARD.md the brief and the per-scene plan
tools/wordmark.py       wordmark geometry → assets/data/wordmark.json
tools/score.py          synthesized, edit-locked score + SFX mix → assets/audio/score.wav
assets/                 vendored GSAP, embedded fonts, score, wordmark data
```

## Commands

```bash
npm run dev      # Studio preview
npm run check    # lint + runtime + layout + motion + contrast
npm run render   # 1080p60 delivery master → renders/avzon-showreel-master.mp4
npm run encode:web  # web deliverable (CRF 19, faststart) → renders/avzon-showreel.mp4
npm run score    # rebuild assets/audio/score.wav (needs numpy, scipy, soundfile)
```

## Credits and licenses

- **Fonts:** Archivo (Omnibus-Type) and Geist Mono (Vercel), both under the SIL Open
  Font License 1.1. The license texts are in `assets/fonts/`.
- **GSAP 3.14.2** (GreenSock) is vendored from npm under the GSAP Standard
  "no charge" License.
- **Sound effects** (impact, whooshes, ping, sparkle, clicks) come from the HyperFrames
  `media-use` bundled library, which sources them from Pixabay under the Pixabay Content
  License. They are mixed into `score.wav`; the raw files are not redistributed here.
- The music bed, riser, stabs, bells, and pad are synthesized in `tools/score.py`.
