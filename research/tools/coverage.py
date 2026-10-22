"""Count lens tags across source notes so INDEX.md and themes.md stay accurate.

Usage: python3 research/tools/coverage.py
"""
import collections
import pathlib
import re

SOURCES = pathlib.Path(__file__).resolve().parent.parent / "sources"
FIELDS = ["players", "value_chain", "stack_layer", "intention_matrix", "themes", "type", "signal", "access"]


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---", text, re.S)
    meta = {}
    for line in (match.group(1) if match else "").splitlines():
        key, _, value = line.partition(":")
        value = value.split("#")[0].strip()
        if value.startswith("["):
            meta[key.strip()] = [v.strip() for v in value.strip("[]").split(",") if v.strip()]
        else:
            meta[key.strip()] = value.strip('"')
    return meta


def main():
    notes = sorted(p for p in SOURCES.glob("S*.md"))
    counts = {field: collections.Counter() for field in FIELDS}
    by_theme = collections.defaultdict(list)
    for note in notes:
        meta = front_matter(note)
        for field in FIELDS:
            values = meta.get(field, [])
            for value in values if isinstance(values, list) else [values]:
                counts[field][value] += 1
        for theme in meta.get("themes", []):
            by_theme[theme].append(meta.get("id", note.stem[:4]))
    print(f"{len(notes)} source notes\n")
    for field in FIELDS:
        print(f"{field}: " + ", ".join(f"{k} x{v}" for k, v in counts[field].most_common()))
    print("\nSources per theme:")
    for theme in sorted(by_theme, key=lambda t: int(t[1:]) if t[1:].isdigit() else 99):
        print(f"  {theme} ({len(by_theme[theme])}): {', '.join(by_theme[theme])}")


if __name__ == "__main__":
    main()
