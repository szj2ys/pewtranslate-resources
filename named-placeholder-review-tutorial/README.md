# Preserve named placeholders when localizing interface text

A standalone tutorial and small Python checker for reviewing named placeholder occurrences. The guide explains the supported grammar, provides synthetic English examples and executed output, and shows where application and terminology review are still necessary.

On the hosted page, use **Download checker.py** or select the complete code example. For a local copy of this project, open `index.html` to read and select the code, or use the bundled `checker.py` directly; the browser download control may not work from a `file://` page. Run the saved or bundled script with:

```sh
python checker.py
```

Use `python3` if that is your Python command. The script uses only the standard library and Python 3.10-compatible syntax; prefer a currently supported release. No packages or account are required.

The supported subset is ASCII named fields such as `{person}`, with escaped literal braces `{{` and `}}`. Counts are case-sensitive. Positional fields, attribute/index access, conversions, explicit format specifications, nested fields and ICU syntax are rejected. Every `%` or `$` character is also rejected, including literal percentages or currency symbols. No automatic corrections are made.

Matching counts do not establish meaning, grammatical correctness, safe rendering or the application's expected placeholder contract. The example renders only fixed, known string values; it is not a general-purpose template renderer.

The page contains no JavaScript, analytics, remote assets or storage. Opening it locally needs no network. Reference links navigate only when activated. The Python checker does not use the network or write files.

Original AI-assisted material by PewTranslate; all examples are fictional. PewTranslate's live translation accounts remain closed. Python and Google do not endorse this tutorial.

MIT licensed; see `LICENSE`.
