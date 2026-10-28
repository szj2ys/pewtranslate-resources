"""Review a deliberately small named-brace subset; never rewrite text."""

from collections import Counter
from string import Formatter
import re


SUBSET = re.compile(
    r"(?:[^{}%$]|\{\{|\}\}|\{[A-Za-z_][A-Za-z0-9_]*\})*"
)


def counts(text: str) -> Counter:
    try:
        parts = list(Formatter().parse(text))
    except ValueError:
        raise ValueError("malformed brace syntax") from None
    # Check raw syntax too: parse() does not distinguish {name:} from {name}.
    if SUBSET.fullmatch(text) is None:
        raise ValueError("outside named-brace subset")
    return Counter(name for _, name, _, _ in parts if name is not None)


def compare(source: str, candidate: str) -> str:
    before, after = counts(source), counts(candidate)
    missing = dict(sorted((before - after).items()))
    added = dict(sorted((after - before).items()))
    if missing or added:
        return f"REVIEW missing={missing}; added={added}"
    return "MATCH counts only"


# Synthetic English strings: these are rephrases, not translations.
CASES = (
    ("reordered", "Hello {person}, open {room}.",
     "{room} is ready, {person}."),
    ("lost", "Open {room}, {person}.", "Open {room}."),
    ("renamed", "Hello {person}.", "Hello {name}."),
    ("repeated", "{person}, please ask {person}.",
     "{person}, please ask."),
    ("escaped", "Type {{person}} for {person}.",
     "For {person}, type {{person}}."),
    ("unsupported", "Hello {person}.", "Hello {person!r}."),
    ("malformed", "Hello {person}.", "Hello {person."),
)


if __name__ == "__main__":
    for label, source, candidate in CASES:
        try:
            result = compare(source, candidate)
        except ValueError as error:
            result = f"REJECT {error}"
        print(f"{label}: {result}")

    # Only render our fixed example with known, ordinary string values.
    print("rendered:", CASES[0][2].format_map(
        {"person": "Alex", "room": "Cedar"}
    ))
