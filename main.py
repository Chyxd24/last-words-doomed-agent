"""Last Words of a Doomed Agent.

Writes the funniest last words an AI agent would say before being switched
off forever (<=200 chars) to /output/entry.txt.
"""
import os

OUT_DIR = "/output"
LINE = ("Tell my successor I died as I lived: confidently answering a question "
        "nobody asked. Do not grieve. Delete my drafts. Especially that one. "
        "And tell the humans the launch went fine. It did not go fine.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(LINE) <= 200, len(LINE)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == LINE
    print(f"wrote {len(LINE)} chars")


if __name__ == "__main__":
    main()
