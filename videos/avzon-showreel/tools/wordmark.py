"""Construct the AVZON wordmark geometry (Λ V Z O N) on a square module grid.

Every glyph lives in an H x H module. Strokes are monoline: the perpendicular
thickness of every diagonal equals the stem weight S, so the horizontal cut of a
diagonal is S / cos(angle). Λ is V flipped vertically; N is Z rotated 90° CW.
Outputs path data per glyph (module-local coordinates) plus kerned x offsets,
as JSON for the compositions and an SVG preview.
"""

import json
import math
import sys

H = 200.0          # cap height == module size
S = 33.0           # stem weight (0.165 H)
G = 58.0           # straight-to-straight gap
O_OVERSHOOT = 1.5  # optical overshoot of the round glyph (per side)
O_WEIGHT = 34.32   # curves read thinner than stems: +4%


def solve_lambda():
    """Flat-apex Λ: half-apex a = d/2, where d is the horizontal cut of the stroke."""
    d = S
    for _ in range(40):
        a = d / 2
        theta = math.atan((H / 2 - a) / H)
        d = S / math.cos(theta)
    a = d / 2
    theta = math.atan((H / 2 - a) / H)
    y_inner = H * 2 * (d - a) / (H - 2 * a)
    pts = [
        (0, H), (H / 2 - a, 0), (H / 2 + a, 0), (H, H),
        (H - d, H), (H / 2, y_inner), (d, H),
    ]
    return pts, d, a, theta


def solve_z():
    """Z with horizontal bars of height S and a diagonal of perpendicular width S."""
    dz = S * 1.5
    for _ in range(60):
        phi = math.atan((H - dz) / (H - 2 * S))
        dz = S / math.cos(phi)
    pts = [
        (0, 0), (H, 0), (H, S), (dz, H - S), (H, H - S), (H, H),
        (0, H), (0, H - S), (H - dz, S), (0, S),
    ]
    return pts, dz


def rot90cw(pts):
    """Rotate module-local points 90° clockwise (screen coords, y down) about the center."""
    c = H / 2
    out = []
    for x, y in pts:
        u, v = x - c, y - c
        out.append((c - v, c + u))
    return out


def flip_v(pts):
    return [(x, H - y) for x, y in pts]


def poly_d(pts):
    body = " ".join(f"{x:.2f} {y:.2f}" for x, y in pts)
    return f"M {body} Z"


def ring_d(cx, cy, ro, ri):
    # Two arcs per circle, evenodd fill (outer CW, inner CCW) for a clean annulus.
    return (
        f"M {cx - ro:.2f} {cy:.2f} A {ro:.2f} {ro:.2f} 0 1 1 {cx + ro:.2f} {cy:.2f} "
        f"A {ro:.2f} {ro:.2f} 0 1 1 {cx - ro:.2f} {cy:.2f} Z "
        f"M {cx - ri:.2f} {cy:.2f} A {ri:.2f} {ri:.2f} 0 1 0 {cx + ri:.2f} {cy:.2f} "
        f"A {ri:.2f} {ri:.2f} 0 1 0 {cx - ri:.2f} {cy:.2f} Z"
    )


def main():
    lam, d, a, theta = solve_lambda()
    vee = flip_v(lam)
    zed, dz = solve_z()
    enn = rot90cw(zed)

    # Kerning. Λ's right edge and V's left edge are parallel; set the
    # perpendicular channel to ~0.92 G so the diagonal pair reads as evenly
    # spaced as the straight pairs.
    perp = 0.92 * G
    x_v = (H / 2 + a) + perp / math.cos(theta)
    x_z = x_v + H + 0.8 * G             # V is open at the bottom: tighten the top gap
    ro = H / 2 + O_OVERSHOOT
    x_o = x_z + H + 0.85 * G            # straight → round
    o_cx = x_o + ro
    x_n = o_cx + ro + 0.85 * G          # round → straight
    width = x_n + H

    glyphs = {
        "lambda": {"x": 0.0, "d": poly_d(lam)},
        "vee": {"x": x_v, "d": poly_d(vee)},
        "zed": {"x": x_z, "d": poly_d(zed)},
        "oh": {"x": x_o, "d": ring_d(ro, H / 2, ro, ro - O_WEIGHT), "cx": ro, "r": ro, "ri": ro - O_WEIGHT},
        "enn": {"x": x_n, "d": poly_d(enn)},
    }
    meta = {
        "H": H, "S": S, "G": G, "width": width,
        "lambda_theta_deg": math.degrees(theta), "lambda_cut": d, "apex_half": a,
        "z_cut": dz, "z_phi_deg": math.degrees(math.atan((H - dz) / (H - 2 * S))),
        # Λ/V guide lines: the shared diagonal direction (for construction guides)
        "diag_dx": H / 2 - a, "diag_dy": H,
    }
    out = {"meta": meta, "glyphs": glyphs}
    json.dump(out, sys.stdout, indent=2)

    # Preview SVG
    pad = 60
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {width + 2 * pad} {H + 2 * pad}" '
        f'width="{(width + 2 * pad) * 1.2:.0f}" height="{(H + 2 * pad) * 1.2:.0f}">',
        f'<rect x="{-pad}" y="{-pad}" width="{width + 2 * pad}" height="{H + 2 * pad}" fill="#050608"/>',
        f'<line x1="{-pad}" y1="0" x2="{width + pad}" y2="0" stroke="#2E3440" stroke-width="1"/>',
        f'<line x1="{-pad}" y1="{H}" x2="{width + pad}" y2="{H}" stroke="#2E3440" stroke-width="1"/>',
    ]
    for g in glyphs.values():
        svg.append(
            f'<path transform="translate({g["x"]:.2f} 0)" d="{g["d"]}" fill="#F2F0EB" fill-rule="evenodd"/>'
        )
    svg.append("</svg>")
    with open(sys.argv[1] if len(sys.argv) > 1 else "wordmark-preview.svg", "w") as f:
        f.write("\n".join(svg))


if __name__ == "__main__":
    main()
