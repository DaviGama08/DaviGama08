#!/usr/bin/env python3
"""Slow README animated WebP previews without changing quality or frame content.

Copies each animation to assets/optimized/slow-*.webp and updates README links.
Only frame duration metadata is edited, so encoded pixels stay byte-identical.
The original animation files are preserved.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUT_DIR = ROOT / "assets" / "optimized"

def frames(data: bytes) -> list[tuple[int, int]]:
    """Return (duration offset, duration ms) for every ANMF chunk."""
    if len(data) < 12 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return []
    offset, found = 12, []
    while offset + 8 <= len(data):
        kind = data[offset:offset + 4]
        size = int.from_bytes(data[offset + 4:offset + 8], "little")
        first = offset + 8
        if first + size > len(data):
            raise ValueError("Invalid WebP chunk size")
        if kind == b"ANMF":
            if size < 16:
                raise ValueError("Invalid ANMF header")
            dur_offset = first + 12
            duration = int.from_bytes(data[dur_offset:dur_offset + 3], "little")
            found.append((dur_offset, duration))
        offset = first + size + (size % 2)
    return found

def total_ms(data: bytes) -> int:
    return sum(max(d, 30) for _, d in frames(data))

def slow_animation(source: Path, original: Path, destination: Path) -> str:
    raw = source.read_bytes()
    chunks = frames(raw)
    if len(chunks) < 2:
        return "Skipped (not animated)"
    current_ms = total_ms(raw)
    reference_ms = total_ms(original.read_bytes()) if original.is_file() else current_ms
    # Aim for a clear, readable playback: at least ~1.9x the optimized duration,
    # and at least slightly slower than the unoptimized original's recorded duration.
    target_ms = max(10000, round(current_ms * 1.9), round(reference_ms * 1.2))
    scale = min(8.0, target_ms / max(current_ms, 1))
    result = bytearray(raw)
    durations = []
    for offset, value in chunks:
        duration = min(0xFFFFFF, max(100, round(max(30, value) * scale)))
        result[offset:offset + 3] = duration.to_bytes(3, "little")
        durations.append(duration)
    if len(result) != len(raw):
        raise AssertionError("Unexpected WebP size change")
    if frames(bytes(result)) != [(pos, dur) for (pos, _), dur in zip(chunks, durations)]:
        raise AssertionError("Frame duration verification failed")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(result)
    return f"{len(chunks)} frames, {current_ms / 1000:.1f}s -> {sum(durations) / 1000:.1f}s"

def main() -> None:
    markdown = README.read_text(encoding="utf-8")
    pattern = re.compile(r'(<img src=")(assets/(?:optimized|portfolio)/)([^"/]+\.webp)("[^>]*alt="Pré-visualização animada de [^"]+"[^>]*>)')
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        prefix, directory, name, suffix = match.groups()
        if name.startswith("slow-"):
            return match.group(0)
        source = ROOT / directory / name
        original = ROOT / "assets" / "portfolio" / name
        if not source.is_file():
            raise FileNotFoundError(source)
        destination = OUT_DIR / f"slow-{name}"
        status = slow_animation(source, original, destination)
        print(f"{name}: {status}", flush=True)
        if status.startswith("Skipped"):
            return match.group(0)
        count += 1
        return f'{prefix}assets/optimized/slow-{name}{suffix}'

    new_markdown = pattern.sub(replace, markdown)
    if count:
        README.write_text(new_markdown, encoding="utf-8")
    if new_markdown.count("<details>") != new_markdown.count("</details>"):
        raise AssertionError("Unbalanced README details")
    print(f"Slowed {count} animated previews. Originals retained.", flush=True)

if __name__ == "__main__":
    main()
