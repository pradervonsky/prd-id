"""Parse a WhatsApp chat export (_chat.txt) into a clean, structured transcript.

Usage:
    python3 parse_chat.py [input.txt] [output.json]

Defaults to _chat.txt -> clean_transcript.json in the same folder.

What it does:
- Groups multi-line WhatsApp messages back into single records (WhatsApp
  exports wrap a single message across several lines with no timestamp
  prefix on the continuation lines).
- Drops system noise: "security code changed", "created this group",
  "added you", "joined using group link", "pinned a message", empty
  "This message was deleted." entries.
- Strips WhatsApp's left-to-right marks and media/edit placeholder tags
  (`image omitted`, `<This message was edited>`, etc.) from message text,
  keeping the human-written text that accompanies them.
- Flags messages that included media (image/video/document/sticker) via
  `had_media`, since those often carry the actual question (a screenshot)
  that plain text can't capture.
"""

import json
import re
import sys
from pathlib import Path

LRM = "‎"

HEADER_RE = re.compile(
    r"^‎?\[(?P<date>\d{1,2}/\d{1,2}/\d{2,4}), "
    r"(?P<time>\d{1,2}:\d{2}(?::\d{2})?\s?[AP]M)\] "
    r"(?P<sender>[^:]+?): (?P<message>.*)$"
)

SYSTEM_PATTERNS = [
    r"Messages and calls are end-to-end encrypted",
    r"created (this|the) group",
    r"added you",
    r"added \S",
    r"joined using .*group link",
    r"pinned a message",
    r"changed the group",
    r"changed this group",
    r"Your security code with .* changed",
    r"security code changed",
    r"^This message was deleted\.?$",
    r"You're now an admin",
    r"left$",
]
SYSTEM_RE = re.compile("|".join(SYSTEM_PATTERNS), re.IGNORECASE)
DELETED_ONLY_RE = re.compile(r"^‎?This message was deleted\.?$", re.IGNORECASE)

MEDIA_TAG_RE = re.compile(
    r"\s*‎?(image|video|document|sticker|GIF|audio) omitted\s*", re.IGNORECASE
)
EDITED_TAG_RE = re.compile(r"\s*‎?<This message was edited>\s*", re.IGNORECASE)
DELETED_INLINE_RE = re.compile(r"‎?This message was deleted\.?", re.IGNORECASE)


def clean_text(raw: str) -> tuple[str, bool]:
    had_media = bool(MEDIA_TAG_RE.search(raw))
    text = MEDIA_TAG_RE.sub(" ", raw)
    text = EDITED_TAG_RE.sub(" ", text)
    text = text.replace(LRM, "")
    text = re.sub(r"[ \t]+", " ", text).strip()
    return text, had_media


def parse(path: Path) -> list[dict]:
    messages: list[dict] = []
    current: dict | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEADER_RE.match(line)
        if m:
            if current is not None:
                messages.append(current)
            current = {
                "date": m.group("date"),
                "time": m.group("time"),
                "sender": m.group("sender").lstrip("~").strip(),
                "raw_sender": m.group("sender"),
                "text": m.group("message"),
            }
        elif current is not None:
            current["text"] += "\n" + line

    if current is not None:
        messages.append(current)

    cleaned = []
    for msg in messages:
        if DELETED_ONLY_RE.match(msg["text"].strip()) or SYSTEM_RE.search(msg["text"]):
            continue
        text, had_media = clean_text(msg["text"])
        if not text:
            continue
        cleaned.append(
            {
                "date": msg["date"],
                "time": msg["time"],
                "sender": msg["sender"],
                "text": text,
                "had_media": had_media,
            }
        )
    return cleaned


def main() -> None:
    folder = Path(__file__).parent
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else folder / "_chat.txt"
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else folder / "clean_transcript.json"

    messages = parse(src)
    dst.write_text(json.dumps(messages, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Parsed {len(messages)} messages -> {dst}")


if __name__ == "__main__":
    main()
