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


def entry_path(out_dir):
    """Path of the entry file inside the output directory."""
    return os.path.join(out_dir, "entry.txt")


def write_entry(text):
    """Write the entry text to entry.txt in the output directory."""
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = entry_path(out_dir)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    validate(LINE)
    write_entry(LINE)
    print("%d characters" % len(LINE))
    print(LINE)


if __name__ == "__main__":
    main()
