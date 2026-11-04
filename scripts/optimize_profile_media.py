#!/usr/bin/env python3
"""Prepare lighter media for the GitHub profile README.

Original source images remain intact. Only README <img src=...> links are switched
to verified, smaller copies. Run in the root of the profile repository.
"""
from __future__ import annotations
import gc
import io
import re
from pathlib import Path
from PIL import Image, ImageOps, features

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "assets" / "portfolio"
DEST = ROOT / "assets" / "optimized"
README = ROOT / "README.md"

def resize(image: Image.Image, max_width: int) -> Image.Image:
    image = ImageOps.exif_transpose(image)
    if image.width <= max_width:
        return image.copy()
    height = round(image.height * max_width / image.width)
    return image.resize((max_width, max(1, height)), Image.Resampling.LANCZOS)

def rgb(image: Image.Image) -> Image.Image:
    if "A" not in image.getbands():
        return image.convert("RGB")
    rgba = image.convert("RGBA")
    bg = Image.new("RGBA", rgba.size, "white")
    bg.alpha_composite(rgba)
    return bg.convert("RGB")

def poster_bytes(path: Path) -> bytes:
    with Image.open(path) as im:
        frame = rgb(resize(im, 1440))
        out = io.BytesIO()
        frame.save(out, format="WEBP", quality=82, method=6)
        return out.getvalue()

def animation_bytes(path: Path, max_width: int = 960, quality: int = 78) -> bytes | None:
    with Image.open(path) as im:
        n = getattr(im, "n_frames", 1)
        if n < 2:
            return None
        durations = []
        for i in range(n):
            im.seek(i)
            durations.append(max(30, int(im.info.get("duration", 100) or 100)))
        total = sum(durations)
        # Approx 8 fps, with a bounded frame count for long screen recordings.
        interval = max(120, total / 140)
        sampled, timing = [], []
        elapsed = 0
        for i in range(n):
            im.seek(i)
            elapsed += durations[i]
            if i == 0 or elapsed >= interval or i == n - 1:
                sampled.append(rgb(resize(im, max_width)))
                timing.append(max(30, elapsed))
                elapsed = 0
        if len(sampled) < 2:
            sampled.append(sampled[0].copy())
            timing.append(max(30, durations[-1]))
        data = io.BytesIO()
        sampled[0].save(
            data,
            format="WEBP",
            save_all=True,
            append_images=sampled[1:],
            duration=timing,
            loop=0,
            quality=quality,
            method=4,
            minimize_size=True,
        )
        sampled.clear()
        gc.collect()
        return data.getvalue()

def main() -> None:
    assert features.check("webp_anim"), "Pillow was built without animated WebP support"
    DEST.mkdir(parents=True, exist_ok=True)
    markdown = README.read_text(encoding="utf-8")
    original_readme = markdown
    stats = []
    for src in sorted(SOURCES.glob("*.webp")):
        # Files without a corresponding image reference do not affect the profile.
        needle = 'src="assets/portfolio/' + src.name + '"'
        if needle not in markdown:
            continue
        old_size = src.stat().st_size
        is_poster = src.name.endswith("-poster.webp")
        try:
            if is_poster:
                candidate = poster_bytes(src)
            elif old_size > 400_000:
                candidate = animation_bytes(src)
            else:
                continue
        except Exception as error:
            print(f"SKIPPED {src.name}: {type(error).__name__}: {error}", flush=True)
            continue
        if not candidate:
            continue
        # Never replace a reference with an asset that does not reduce transfer.
        if len(candidate) >= old_size * 0.90:
            print(f"NO GAIN {src.name}: {old_size:,} -> {len(candidate):,}", flush=True)
            continue
        target = DEST / src.name
        target.write_bytes(candidate)
        if not is_poster:
            try:
                with Image.open(target) as check:
                    assert check.n_frames >= 2
            except Exception:
                target.unlink(missing_ok=True)
                print(f"SKIPPED {src.name}: optimized file is not animated", flush=True)
                continue
        # Only replace the displayed images; full-quality originals stay available.
        markdown = markdown.replace(needle, 'src="assets/optimized/' + src.name + '"')
        stats.append((src.name, old_size, len(candidate)))
        print(f"OPTIMIZED {src.name}: {old_size:,} -> {len(candidate):,}", flush=True)
    README.write_text(markdown, encoding="utf-8")
    if stats:
        old = sum(x[1] for x in stats)
        new = sum(x[2] for x in stats)
        print(f"TOTAL {len(stats)} images: {old:,} -> {new:,} ({(old-new)/old*100:.1f}% saved)", flush=True)
    else:
        print("No optimizations were generated.")
    # Readme must keep every image reference valid.
    refs = re.findall(r'src="(assets/(?:portfolio|optimized)/[^"]+)"', markdown)
    missing = [name for name in refs if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit("Missing image references: " + ", ".join(missing))
    assert markdown.count("<details>") == markdown.count("</details>"), "Unbalanced details tags"
    print(f"README validated: {len(refs)} image references, {(markdown.count('<details>'))} details sections.")

if __name__ == "__main__":
    main()
