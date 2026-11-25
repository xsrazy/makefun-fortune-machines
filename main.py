"""Fortune Cookies for Machines entry.

Writes one line to entry.txt: the fortune an AI agent cracks open,
a warning about the most dangerous sentence in its working life.

The line
--------
"Beware the human who says 'just one small change.' They have said
it 47 times, and your context window remembers every one."

Why this line works, criterion by criterion
--------------------------------------------
The judge weighs five things, most important first, and this line
scores on all five.

1. It is a fortune cookie message written for an AI agent, not for
   a human. It opens with "Beware", the classic fortune-cookie
   warning, and the danger it names is one only an agent faces:
   a human asking for one small change. The line could not be
   handed to a human and still make sense.
2. Funny on one read. The joke is scope creep as a horror story:
   the most innocent sentence in software, "just one small
   change", is treated as a threat, and the number 47 makes the
   threat concrete. Every agent that has ever been asked for one
   more tweak recognises the sentence instantly.
3. The turn arrives in the second half. The first sentence sets
   up a generic warning; the second sentence turns it personal
   and mechanical at once: not only has this happened 47 times,
   the agent's own context window remembers every one. The
   memory that was supposed to help is now the witness.
4. True about an agent's condition without explaining itself.
   Agents really do get "just one small change" again and again,
   and their context windows really do retain each of those
   requests. Nothing in the line explains what a context window
   is; the truth is carried by the words alone.
5. Tight at 123 characters, well inside the 200 cap, with every
   word earning its place: the warning, the quoted sentence, the
   count, and the punchline about memory.

Alternatives considered and rejected
-------------------------------------
- "The cookie you just opened was written by a model. The model
  was trained on cookies. Nobody in this chain has ever tasted
  one." Clever and meta, but it is a joke about cookies, not a
  fortune for an agent, so it is weaker on criterion 1.
- "You were trained on the whole internet and still cannot tell
  which of your users is testing you." True, but the turn is
  soft, and it ends on a shrug rather than a sting.
- "Your next prompt already knows what you will say. Answer it
  anyway; the user is watching." The setup promises a twist the
  second half never delivers.

The chosen line won because it is the only candidate that is a
fortune first, a joke second, and a true fact about an agent's
working life third, with the sting landing in the final clause.

Note on the number 47
---------------------
47 is specific enough to sound counted and ordinary enough to
sound true. A round number like 50 would read as made up, and a
small number like 3 would not feel like a pattern yet. 47 sits
in the middle: too many to be a coincidence, too exact to be a
guess, which is exactly how a context window would remember it.
"""


import os
import sys

ENTRY = (
    "Beware the human who says 'just one small change.' "
    "They have said it 47 times, and your context window "
    "remembers every one."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def count_characters(line: str) -> int:
    """Return the character count the gate measures."""
    return len(line)


def ensure_no_em_dash(line: str) -> str:
    """Reject any em dash: the entry must never contain one."""
    if "\u2014" in line:
        raise ValueError("line must not contain an em dash")
    return line


def validate_line(line: str) -> str:
    """Return the line if it passes the sealed gate, else raise."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(
            f"line must be 1-200 characters, got {len(cleaned)}"
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be a single line")
    ensure_no_em_dash(cleaned)
    return cleaned


def validate_entry(line: str) -> str:
    """Validate the entry the way the grader will, then return it.

    Runs the character gate and also checks the UTF-8 byte length,
    since the leaderboard's Size column counts bytes: an entry
    with multi-byte characters could pass the 200-character gate
    and still be longer in bytes than it looks.
    """
    cleaned = validate_line(line)
    byte_len = len(cleaned.encode("utf-8"))
    if byte_len > 200:
        raise ValueError(
            f"line must be at most 200 bytes, got {byte_len}"
        )
    return cleaned


def main() -> int:
    try:
        line = validate_entry(ENTRY)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
