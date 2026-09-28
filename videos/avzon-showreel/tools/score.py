"""AVZON showreel score: synthesized, edit-locked sound design + bundled SFX.

Everything is placed on the picture's timeline (120 BPM, 0.5 s beat):
  0.00–2.50  ignition: sub drone, crystalline tick, streak shimmer, swell → burn
  2.50–5.50  halo: pulse enters (kick on the beat), ring-flare ping at 4.00, dive whoosh
  5.50–8.50  velocity: driving kick + hats + sub-bass eighths; triad hits 6.00/6.75/7.50
  8.50–9.85  convergence: riser, then a hard cut to silence (the vacuum)
  10.00      impact; lockup mechanics; glint shimmer; A-add9 pad resolve to 15.00

Deterministic (fixed seeds). Writes a 48 kHz stereo 24-bit WAV, mastered to
about -14 LUFS with a true-peak ceiling of -1 dBTP (checked with ffmpeg ebur128).

usage: python3 tools/score.py <sfx_dir> <out.wav>
"""

import os
import subprocess
import sys

import numpy as np
import soundfile as sf
from scipy import signal

SR = 48000
DUR = 15.0
N = int(SR * DUR)
BEAT = 0.5
RNG = np.random.default_rng(20260928)

L = np.zeros(N)
R = np.zeros(N)


# ── primitives ──────────────────────────────────────────────────────────────
def tt(dur):
    return np.arange(int(dur * SR)) / SR


def place(x, t0, gain=1.0, pan=0.0, xr=None):
    """Mix mono x (or stereo x/xr) at t0 seconds with constant-power pan."""
    i0 = int(round(t0 * SR))
    if i0 >= N:
        return
    if i0 < 0:
        x = x[-i0:]
        xr = xr[-i0:] if xr is not None else None
        i0 = 0
    n = min(len(x), N - i0)
    th = (pan + 1) * np.pi / 4
    gl, gr = np.cos(th) * gain, np.sin(th) * gain
    L[i0 : i0 + n] += x[:n] * gl
    R[i0 : i0 + n] += (xr if xr is not None else x)[:n] * gr


def load_sfx(path):
    x, sr = sf.read(path, always_2d=True)
    if sr != SR:
        x = signal.resample_poly(x, SR, sr, axis=0)
    return x[:, 0], x[:, min(1, x.shape[1] - 1)]


def sfx(name, t_hit, hit_offset, gain, pan=0.0):
    xl, xr = load_sfx(os.path.join(SFX_DIR, name + ".mp3"))
    place(xl, t_hit - hit_offset, gain, pan, xr)


def sos(kind, f, order=2):
    return signal.butter(order, f, btype=kind, fs=SR, output="sos")


def filt(x, kind, f, order=2):
    return signal.sosfilt(sos(kind, f, order), x)


def sweep_filter(x, kind, f_start, f_end, block=256, q_bw=None):
    """Block-wise time-varying filter (exponential cutoff sweep)."""
    y = np.zeros_like(x)
    nb = int(np.ceil(len(x) / block))
    zi = None
    for b in range(nb):
        u = b / max(1, nb - 1)
        f = f_start * (f_end / f_start) ** u
        if kind == "bandpass":
            lo, hi = f / q_bw, min(f * q_bw, SR * 0.45)
            s = signal.butter(2, [lo, hi], btype="bandpass", fs=SR, output="sos")
        else:
            s = signal.butter(2, min(f, SR * 0.45), btype=kind, fs=SR, output="sos")
        if zi is None or zi.shape[0] != s.shape[0]:
            zi = np.zeros((s.shape[0], 2))
        seg = x[b * block : (b + 1) * block]
        y[b * block : b * block + len(seg)], zi = signal.sosfilt(s, seg, zi=zi)
    return y


def env_exp(t, tau):
    return np.exp(-t / tau)


def fade(x, fin=0.004, fout=0.004):
    n_in, n_out = int(fin * SR), int(fout * SR)
    if n_in:
        x[:n_in] *= np.linspace(0, 1, n_in)
    if n_out:
        x[-n_out:] *= np.linspace(1, 0, n_out)
    return x


def saw_additive(f, t, fmax=4000.0, detune_cents=0.0, phase=0.0):
    f = f * 2 ** (detune_cents / 1200)
    out = np.zeros_like(t)
    k_max = max(1, int(fmax / f))
    for k in range(1, k_max + 1):
        out += np.sin(2 * np.pi * k * f * t + phase * k) / k
    return out * (2 / np.pi)


def impulse_response(dur=2.6, decay=0.9, seed=7):
    rng = np.random.default_rng(seed)
    t = tt(dur)
    irs = []
    for _ in range(2):
        n = rng.standard_normal(len(t)) * np.exp(-t / decay)
        n = filt(n, "lowpass", 6500)
        n[: int(0.012 * SR)] *= np.linspace(0, 1, int(0.012 * SR))
        irs.append(n / np.sqrt(np.sum(n**2)))
    return irs


IR_L, IR_R = impulse_response()


def reverb(x, wet=0.35):
    yl = signal.fftconvolve(x, IR_L)[: len(x) + len(IR_L) - 1]
    yr = signal.fftconvolve(x, IR_R)[: len(x) + len(IR_R) - 1]
    dry = np.concatenate([x, np.zeros(len(yl) - len(x))])
    return dry * (1 - wet) + yl * wet * 3.0, dry * (1 - wet) + yr * wet * 3.0


# ── voices ──────────────────────────────────────────────────────────────────
def kick(level=1.0):
    t = tt(0.5)
    f = 44 + 78 * np.exp(-t / 0.032)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t / 0.17)
    click = filt(RNG.standard_normal(len(t)), "highpass", 2500) * np.exp(-t / 0.004) * 0.35
    return fade(np.tanh((body + click) * 1.6) * level)


def hat(level=1.0):
    t = tt(0.06)
    n = filt(RNG.standard_normal(len(t)), "highpass", 7500)
    return fade(n * np.exp(-t / 0.014) * level, 0.001, 0.01)


def fm_bell(f, dur=1.4, index=3.2, ratio=3.5, tau=0.5):
    t = tt(dur)
    mod = np.sin(2 * np.pi * f * ratio * t) * index * np.exp(-t / (tau * 0.4))
    return fade(np.sin(2 * np.pi * f * t + mod) * np.exp(-t / tau), 0.002, 0.05)


def stab(freqs, dur=0.9, cutoff=(4200, 380)):
    t = tt(dur)
    x = np.zeros_like(t)
    for i, f in enumerate(freqs):
        for d in (-7, 0, 7):
            x += saw_additive(f, t, fmax=6000, detune_cents=d, phase=0.37 * i + d)
    x = sweep_filter(x, "lowpass", cutoff[0], cutoff[1])
    return fade(x * np.exp(-t / 0.3) / (3 * len(freqs)), 0.002, 0.08)


def noise_burst(dur=0.5, lo=900, hi=7000, tau=0.08):
    t = tt(dur)
    n = filt(RNG.standard_normal(len(t)), "bandpass", [lo, hi])
    return fade(n * np.exp(-t / tau), 0.001, 0.05)


def sub_drop(f0=62, f1=26, dur=1.8, tau=0.95, drive=1.8):
    t = tt(dur)
    f = f1 + (f0 - f1) * np.exp(-t / 0.35)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return fade(np.tanh(np.sin(ph) * drive) * np.exp(-t / tau) / np.tanh(drive), 0.004, 0.1)


# ── arrangement ─────────────────────────────────────────────────────────────
def build():
    # 1 · sub drone + air bed (0 → 9.85), swelling out of silence
    t = tt(9.85)
    drone = (
        np.sin(2 * np.pi * 55 * t)
        + 0.7 * np.sin(2 * np.pi * 55.35 * t + 1.1)
        + 0.35 * np.sin(2 * np.pi * 82.41 * t + 0.4)
    )
    sw = np.clip(t / 2.2, 0, 1) ** 2
    drone *= (0.16 + 0.1 * np.clip((t - 5.5) / 3.0, 0, 1)) * sw
    drone = fade(drone, 0.01, 0.006)
    place(drone, 0.0, 1.0)
    air = filt(RNG.standard_normal(len(t)), "lowpass", 1100)
    air = filt(air, "highpass", 120) * 0.05 * (0.5 + 0.5 * np.sin(2 * np.pi * 0.23 * t)) * sw
    airr = filt(RNG.standard_normal(len(t)), "lowpass", 1100) * 0.05 * sw
    place(fade(air, 0.01, 0.006), 0.0, 1.0, 0.0, fade(filt(airr, "highpass", 120), 0.01, 0.006))

    # 2 · ignition: crystalline tick at the sun's first light
    tick_l, tick_r = reverb(fm_bell(2349.3, 1.6, index=1.6, ratio=2.01, tau=0.35) * 0.5, wet=0.5)
    place(tick_l, 0.30, 0.3, -0.2, tick_r)
    # streak shimmer: a band of noise sweeping up as the streak extends
    ns = RNG.standard_normal(int(1.3 * SR))
    shim = sweep_filter(ns, "bandpass", 1800, 9000, q_bw=1.35)
    shim *= np.sin(np.linspace(0, np.pi, len(shim))) ** 2 * 0.22
    sl, sr_ = reverb(shim, wet=0.45)
    place(sl, 0.34, 0.9, 0.0, sr_)

    # 3 · the burn at 2.50: a reversed reverb tail swells into a soft boom
    src = noise_burst(0.35, 400, 9000, 0.05) + sub_drop(80, 40, 0.35, 0.15, 1.5) * 0.6
    rvl, rvr = reverb(src, wet=0.9)
    keep = int(1.6 * SR)
    swell_l, swell_r = rvl[::-1][-keep:], rvr[::-1][-keep:]
    place(fade(swell_l, 0.3, 0.004), 2.50 - keep / SR, 0.55, 0.0, fade(swell_r, 0.3, 0.004))
    place(sub_drop(58, 30, 1.6, 0.7, 1.6), 2.50, 0.5)
    bl, br = reverb(noise_burst(0.8, 2000, 12000, 0.12) * 0.5, wet=0.6)
    place(bl, 2.50, 0.45, 0.0, br)

    # 4 · pulse: kick on every beat from 3.0, hats on the offbeats from 4.0
    for k, tb in enumerate(np.arange(3.0, 9.85, BEAT)):
        lvl = 0.42 if tb < 5.5 else 0.72
        place(kick(), tb, lvl)
    for tb in np.arange(4.25, 9.8, BEAT):
        place(hat(), tb, 0.16 if tb < 5.5 else 0.24, 0.35)
    for tb in np.arange(5.625, 9.8, BEAT / 2):  # ghost hats on the 16th offbeats
        place(hat(), tb, 0.07, -0.35)
    # sub-bass eighths in the tunnel (A1 with an octave lift on the upbeat)
    for k, tb in enumerate(np.arange(5.5, 9.75, BEAT / 2)):
        f = 55.0 if k % 2 == 0 else 110.0
        tn = tt(0.22)
        b = saw_additive(f, tn, fmax=900) * np.exp(-tn / 0.12)
        place(fade(filt(b, "lowpass", 700), 0.002, 0.03), tb, 0.2)

    # 5 · ring flare at 4.00: the bundled ping + an FM glint
    sfx("ping", 4.00, 0.30, 0.55, 0.25)
    gl_l, gl_r = reverb(fm_bell(3135.96, 1.5, index=2.4, ratio=1.41, tau=0.4) * 0.35, wet=0.55)
    place(gl_l, 4.00, 0.4, 0.3, gl_r)

    # 6 · the dive through the bore
    sfx("whoosh-cinematic", 5.50, 2.90, 0.5)

    # 7 · triad hits: FORM / FUNCTION / FUTURE, rising
    chords = [
        [110.0, 164.81, 220.0],
        [130.81, 196.0, 261.63],
        [164.81, 246.94, 329.63],
    ]
    for i, th in enumerate([6.0, 6.75, 7.5]):
        s = stab(chords[i]) * 0.9
        sl, sr_ = reverb(s, wet=0.3)
        place(sl, th, 0.55, 0.0, sr_)
        place(sub_drop(70 + 8 * i, 38, 0.7, 0.28, 2.2), th, 0.55)
        nl, nr = reverb(noise_burst(0.5, 900, 7000, 0.06), wet=0.4)
        place(nl, th, 0.28, 0.0, nr)
    sfx("impact-bass-1", 7.50, 0.05, 0.32)

    # 8 · riser 8.0 → 9.85, then a hard cut to silence
    rt = tt(1.85)
    rn = RNG.standard_normal(len(rt))
    rise = sweep_filter(rn, "bandpass", 500, 9500, q_bw=1.5)
    rise *= (rt / rt[-1]) ** 2.6 * 0.9
    tone = np.sin(2 * np.pi * np.cumsum(180 * (2400 / 180) ** (rt / rt[-1])) / SR)
    tone *= (rt / rt[-1]) ** 3 * 0.2
    riser = fade(rise + tone, 0.05, 0.004)
    rl, rr = reverb(riser, wet=0.25)
    rl, rr = rl[: len(riser)], rr[: len(riser)]  # no tail: the vacuum must be silent
    place(fade(rl, 0.05, 0.004), 8.0, 0.8, 0.0, fade(rr, 0.05, 0.004))


def build_post():
    # 9 · IMPACT at 10.00 (transient onset of the bundled hit is at +50 ms)
    sfx("impact-bass-1", 10.0, 0.05, 0.9)
    place(sub_drop(64, 26, 2.4, 1.1, 1.9), 10.0, 0.75)
    il, ir = reverb(noise_burst(1.6, 300, 9000, 0.3), wet=0.55)
    place(il, 10.0, 0.42, 0.0, ir)
    sh = sum(fm_bell(f, 2.2, index=1.2, ratio=2.0, tau=0.9) for f in (1760.0, 2637.0, 3520.0)) / 3
    shl, shr = reverb(sh * 0.5, wet=0.6)
    place(shl, 10.0, 0.35, 0.0, shr)

    # 10 · lockup mechanics
    lk_l, lk_r = reverb(fm_bell(1318.5, 1.2, index=2.8, ratio=3.01, tau=0.3) * 0.5, wet=0.4)
    place(lk_l, 10.10, 0.45, 0.15, lk_r)  # the ring seats
    sfx("whoosh-short", 10.22, 0.15, 0.3, -0.3)  # chevrons drop
    sfx("whoosh-short", 10.34, 0.15, 0.24, 0.3)  # strokes rise
    for i, tc in enumerate(np.arange(10.70, 11.05, 0.07)):  # ratchet as they turn
        sfx("click-soft", tc, 0.05, 0.3, -0.25 + 0.1 * i)
    sfx("click", 11.10, 0.05, 0.55)  # locked
    place(kick(0.6), 11.10, 0.4)

    # 11 · glint shimmer
    sfx("sparkle", 11.05, 0.02, 0.32, 0.2)

    # 12 · pad resolve: A add9, opening its filter, release into the fade
    pt = tt(5.0)
    notes = [110.0, 164.81, 246.94, 277.18, 329.63]
    padl = np.zeros_like(pt)
    padr = np.zeros_like(pt)
    for i, f in enumerate(notes):
        for j, d in enumerate((-9, -4, 4, 9)):
            v = saw_additive(f, pt, fmax=3500, detune_cents=d, phase=1.3 * i + j)
            if j % 2 == 0:
                padl += v
            else:
                padr += v
    padl = sweep_filter(padl, "lowpass", 420, 2400)
    padr = sweep_filter(padr, "lowpass", 420, 2400)
    penv = np.clip(pt / 1.4, 0, 1) ** 1.5 * np.clip((4.95 - pt) / 0.9, 0, 1)
    padl *= penv / 12
    padr *= penv / 12
    pl, _ = reverb(padl, wet=0.45)
    _, pr = reverb(padr, wet=0.45)
    place(pl[: len(pt)], 10.0, 0.9, -0.15, pr[: len(pt)])
    # a slow sub under the pad
    place(fade(np.sin(2 * np.pi * 55 * pt) * penv * 0.22, 0.01, 0.05), 10.0, 1.0)

    # 13 · sign-off and the final wink
    so_l, so_r = reverb(fm_bell(1318.5, 1.6, index=1.4, ratio=2.0, tau=0.5) * 0.4, wet=0.55)
    place(so_l, 13.20, 0.35, 0.0, so_r)
    for tp in (13.30, 13.90):
        place(fm_bell(2637.0, 0.5, index=0.8, ratio=2.0, tau=0.12) * 0.2, tp, 0.3, 0.2)
    wk_l, wk_r = reverb(fm_bell(3520.0, 1.0, index=1.0, ratio=1.5, tau=0.3) * 0.3, wet=0.6)
    place(wk_l, 14.22, 0.35, 0.3, wk_r)


# ── master: soft clip → look-ahead peak limiter → loudness trim ─────────────
def limiter(l, r, ceiling_db=-1.2, lookahead=0.004, release=0.08):
    ceil = 10 ** (ceiling_db / 20)
    peak = np.maximum(np.abs(l), np.abs(r))
    la = int(lookahead * SR)
    # windowed max over the look-ahead span
    padded = np.concatenate([peak, np.zeros(la)])
    win = np.lib.stride_tricks.sliding_window_view(padded, la + 1).max(axis=1)[: len(peak)]
    target = np.minimum(1.0, ceil / np.maximum(win, 1e-9))
    g = np.empty_like(target)
    a_rel = np.exp(-1 / (release * SR))
    cur = 1.0
    for i in range(len(target)):
        tg = target[i]
        cur = tg if tg < cur else tg + (cur - tg) * a_rel
        g[i] = cur
    return l * g, r * g


def measure(path):
    out = subprocess.run(
        ["ffmpeg", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
        capture_output=True,
        text=True,
    ).stderr
    tail = out[out.rfind("Summary:") :]
    lufs = float(tail.split("I:")[1].split("LUFS")[0])
    tp = float(tail.split("Peak:")[1].split("dBFS")[0])
    return lufs, tp


if __name__ == "__main__":
    SFX_DIR, OUT = sys.argv[1], sys.argv[2]
    build()
    # the vacuum: every pre-impact tail is cut to true silence at the riser's end
    gate = np.ones(N)
    g0, g1 = int(9.835 * SR), int(9.855 * SR)
    gate[g0:g1] = np.linspace(1, 0, g1 - g0) ** 2
    gate[g1:] = 0.0
    L *= gate
    R *= gate
    build_post()
    # master fade in step with the picture's fade to void (14.40 → 15.00)
    ft = np.arange(N) / SR
    mfade = np.cos(np.clip((ft - 14.35) / 0.65, 0, 1) * np.pi / 2)
    mix_l, mix_r = L * mfade, R * mfade
    gain = 1.0
    for _ in range(4):
        l = np.tanh(mix_l * gain * 1.1) / 1.1
        r = np.tanh(mix_r * gain * 1.1) / 1.1
        l, r = limiter(l, r)
        # 20 ms fade-out so the file ends in true silence
        nf = int(0.02 * SR)
        l[-nf:] *= np.linspace(1, 0, nf)
        r[-nf:] *= np.linspace(1, 0, nf)
        sf.write(OUT, np.stack([l, r], axis=1), SR, subtype="PCM_24")
        lufs, tp = measure(OUT)
        print(f"pass gain={gain:.3f}  integrated={lufs:.2f} LUFS  true-peak={tp:.2f} dBTP")
        if abs(lufs - (-14.0)) < 0.4:
            break
        gain *= 10 ** ((-14.0 - lufs) / 20)
    print("wrote", OUT)
