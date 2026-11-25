"""Robot Romance: One-Line Pickup Lines for AI.

The entry: one single-line pickup line aimed at a robot/AI,
written to /output/entry.txt.
"""

import os

LINE = "I sampled a thousand futures; in all of them, you stayed."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Check the gate: UTF-8 text, 1-200 characters, not only whitespace,
    a single line. Raises ValueError with the failing rule."""
    text.encode("utf-8")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "length %d outside %d-%d characters" % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("text is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")
    return True


def resolve_output_dir():
    """Output directory: the grader's $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    validate(LINE)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("%d characters" % len(LINE))
    print(LINE)


if __name__ == "__main__":
    main()
