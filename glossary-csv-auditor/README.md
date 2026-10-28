# Glossary CSV auditor

A standalone local tool for reviewing an arbitrary bilingual term sheet: paste comma-separated CSV, explicitly select its source and target columns, inspect exact-string candidates, and export a handoff with original record and physical-line references.

Open `index.html` in a modern browser. No build, account, installation, server or network connection is required. The synthetic example uses fictional English draft labels, not approved translations.

## Reader journey

1. Paste CSV or choose **Load synthetic example**.
2. Explicitly choose whether record 1 contains headers, then **Parse and inspect columns**.
3. Read the positional column labels and up to three parsed data examples per column. Empty or duplicate header labels retain their distinct column numbers. No source/target mapping is guessed.
4. Select two different column positions and **Audit selected columns**.
5. Review candidates using CSV record numbers, physical line spans, a reference to an earlier/contrasting record where relevant, and the original record preview. **Select record** returns to its exact source range without editing it.
6. Download all findings as CSV. Editing the input, header choice or mapping invalidates old findings and disables their export. Reset clears everything; refreshing loses the working data.

## What the checks mean

- **Empty source/target:** the selected field has exactly zero characters. Whitespace-only fields are not empty. No trimming takes place.
- **Exact repeated pair:** both selected strings match an earlier pair exactly. The later occurrence references the first such pair. Other columns may differ; this is not a finding that the entire row is a duplicate.
- **Same source, different targets:** every record in a source group with more than one exact target is flagged, with one contrasting record as a reference. Different contexts may justify different wording. This is **not proof of a wrong translation** and does not enumerate every possible pair.

Empty strings participate in pair/group comparisons, so findings can overlap. Case, spaces, punctuation and Unicode composition are significant. The tool does not translate, casefold, normalize, repair, merge or remove records. A result with no findings does not approve meaning, language support, translation quality or provider-import compatibility.

## Chosen CSV dialect

This implementation is informed by [RFC 4180](https://www.rfc-editor.org/info/rfc4180/), with its dialect stated explicitly rather than claiming full standards certification:

- Comma is the only delimiter. Tabs and semicolons are data, not inferred separators. Unicode text is accepted.
- Double quotes may surround a whole field. Inside a quoted field, doubled double quotes represent one quote. Commas and physical newlines inside quotes belong to the field.
- A quote must occur at the start of its field. After a closing quote, only a comma, record break or end is accepted. Spaces before a quoted field or after its closing quote are not silently ignored.
- Unquoted fields preserve spaces exactly. A trailing comma creates a final empty field. A terminal record break does not create a phantom record. An interior blank line is a one-empty-field record and is not skipped.
- All records must have the same number of fields as record 1. Malformed quotes stop parsing with the current record and physical line; no partial glossary audit or export is produced. Ragged records are listed as structural findings and can be exported, but source/target auditing is blocked until the structure is corrected.
- The header choice is mandatory and explicit. Empty input, header-only input, fewer than two columns and same-column mapping are separate unusable states. Empty and repeated header names remain usable through column positions.
- Browser textareas normalize CRLF and CR to LF, including inside quoted fields. Parsing uses that browser value. The tool does not preserve original file bytes or pre-paste line endings. A pasted BOM is ordinary field content and is not stripped; before an opening quote it can therefore cause a strict quoting error.
- Unpaired UTF-16 surrogate units are rejected explicitly, because converting them to raw UTF-8 CSV would lose the original units. This is not an encoding-detection or Unicode-conformance tool.

The editor scrolls long physical lines horizontally instead of wrapping them. Parsed previews wrap separately for reading.

CSV record numbers are **one-based and include the header**, when present. Physical line start/end values are also one-based and inclusive. An embedded quoted newline increments the physical line but does not start a new CSV record. Selected editor ranges preserve the exact record syntax and omit only its terminating record break.

## Bounds and exports

Input is bounded at **64,000 UTF-16 code units**, **500 CSV records including a header**, **50 columns**, **20,000 cells** and **1,000 physical lines**. Limits apply to the complete parse; excess produces no partial audit. Clipboard pastes that would exceed the input-size or physical-line bound are rejected while retaining existing text. At most 100 findings are added per display step; the CSV includes every finding. Parsed column previews and record previews are visibly shortened where necessary, while full values remain in memory and the export.

Grouping uses exact source strings and target strings, with one reference per finding. It does not generate a quadratic list of every possible pair. A single data record can produce multiple findings.

The findings CSV has 13 columns: Finding, CSV record, Physical line start, Physical line end, Source column, Target column, Source field, Target field, Related CSV record, Related line span, Original record text, Review note, and Protective prefix added to. Column positions are one-based. Structural-only exports leave mapping and selected-field columns empty.

All output fields are quoted, quotes are doubled, rows end with CRLF and the file includes a UTF-8 BOM. Source/target strings and original record syntax are preserved except for explicit spreadsheet protection: cells beginning with `=`, `+`, `-` or `@` after leading whitespace/control characters, or beginning with a tab/newline, receive a leading apostrophe. The final column lists the fields that received this prefix. It is export-only; the editor and comparisons remain unchanged. Keep protective prefixes when opening untrusted content in a spreadsheet. Spreadsheet import behavior varies.

## Privacy and human review

All processing stays in page memory. There are no external scripts, fonts, analytics, storage calls or automatic network requests. A restrictive meta content security policy blocks connections and external assets. Markup is rendered as literal text, and string previews are isolated from surrounding labels. Reference links leave the tool only when followed.

The [PewTranslate glossary-preparation guide](https://pewtranslate.com/en/guides/prepare-sermon-translation-glossary) explains how to record context and involve a competent language reviewer. This auditor helps locate structural candidates; it cannot decide the right wording.

AI-assisted original code by [PewTranslate](https://pewtranslate.com/). Live-translation accounts are closed. No professional certification, actual congregation use, approved translations or working production translation service is claimed.

## Publication and license

Public files: `index.html`, `README.md`, `LICENSE`. Exclude `.verification/`, which contains local tests, downloaded findings and screenshots. Original code and documentation are MIT licensed, copyright 2026 szj2ys.
