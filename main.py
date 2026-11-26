import os

LINE = "I sampled a thousand futures; in all of them, you stayed."


def entry_text():
    return LINE + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(entry_text())


if __name__ == "__main__":
    main()
