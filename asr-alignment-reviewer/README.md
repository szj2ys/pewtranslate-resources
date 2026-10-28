# Literal Transcript Alignment Reviewer

An offline reviewer for two transcript excerpts covering the same segment. It aligns literal tokens, locates substitutions/deletions/insertions in the original editor values, and downloads a complete JSON handoff. It does not listen to audio, transcribe, translate, correct text or grade meaning and intelligibility.

Open `index.html` in a modern browser with JavaScript enabled. No installation, account, package or server is needed. Reference links are optional external navigation.

## Reader workflow

1. Check a reference transcript against the actual recording. An outline, translation or paraphrase is not a matching reference.
2. Paste that reference and the ASR draft for the same short segment, or load the clearly fictional English example.
3. Choose **Compare transcripts**. Read the token rules, counts and any alignment-tie notice.
4. Review each aligned pair. **Select reference/draft token** selects that exact occurrence in its original editor without changing text.
5. Download the complete JSON handoff. It contains both supplied texts; share it deliberately. Resolve differences by returning to the recording and involving the appropriate reviewer.

Loading the example or clearing nonempty editors asks before replacing text. Cancel retains the current input and results. Editing either side invalidates old results and export. Refresh discards the working state.

## Exact comparison rules

Separators are only ASCII space U+0020 and U+0009–U+000D (tab, line feed, vertical tab, form feed, carriage return). Runs between separators are tokens; consecutive separators create no empty token. Case, punctuation, numbers, all other spaces and Unicode code units remain literal. There is no trim, case folding, spelling conversion, contraction expansion or Unicode normalization. Separator-only differences can disappear from the metric. Unspaced text can be one token: this is not universal linguistic word segmentation.

The page preserves current textarea values. Browsers may normalize pasted CRLF/CR line endings to LF. Token positions are zero-based UTF-16 `[start,end)` ranges in those editor values, not original file bytes. Supplementary characters use two units. A gap has no token or position. Quoted previews escape non-ASCII/control units; selection exposes the original text. JSON can reversibly represent even isolated surrogate units.

Alignment transforms reference into draft, minimizing total cost. Exact match costs 0; substitution, deletion and insertion cost 1 each. Backtracking starts at the end and prefers a diagonal pair (match/substitution), then deletion, then insertion on equal cost. A tie notice identifies an alternative optimal predecessor on the chosen path; equal-cost paths can assign different operations and locations. This is not NIST/SCLITE equivalence: SCLITE documents different default alignment weights and richer options.

With reference count N, draft count H, exact matches C, substitutions S, deletions D and insertions I:

- N = C + S + D; H = C + S + I.
- Minimum distance = S + D + I.
- Literal token difference rate = 100 × distance / N. The screen rounds to two decimal places; JSON retains the calculated number and counts. Values above 100% are possible.
- With N = 0, the rate is undefined and exported as `null`, even if both inputs are empty. Counts and alignment remain inspectable.

Operations describe literal differences relative to a supplied reference, not verified errors. No accuracy percentage, model benchmark, semantic assessment, linguistic verdict or readiness threshold is supplied. A lower rate does not establish preserved meaning.

## Bounds and export

Each editor permits at most 32,000 UTF-16 units and 700 tokens. The full `(N+1) × (H+1)` matrix may contain at most 350,000 cells. All bounds are checked before matrix allocation; excess rejects the comparison without truncation or partial output. Work yields after each 32 reference rows, and obsolete runs cannot overwrite a newer editor state.

The page initially displays at most 100 alignment rows, with **Show next rows** for the remainder. The JSON always includes the complete alignment and token arrays, source ranges, exact editor values, rules/version, costs, tie policy, counts, rate, matrix size and limitations. It is not a spreadsheet or corrected transcript. All non-ASCII code units are escaped in the downloaded JSON; decoding restores their exact values.

## Privacy, sources and ownership

The page uses no network requests, audio access, analytics, cookies, persistent storage, external assets or packages. Processing stays in page memory. A restrictive content security policy blocks network connections. Only activating a reference link navigates externally; a deliberate download writes the report on the reader's device.

The [PewTranslate transcript-review guide](https://pewtranslate.com/en/guides/check-sermon-transcript-translation-errors) explains the human follow-up. Primary background references are the [NIST metric definition](https://trec.nist.gov/pubs/trec9/sdrt9_slides/tsld017.htm), [SCLITE documentation](https://github.com/usnistgov/SCTK/blob/master/doc/sclite.htm) and [Speechmatics evaluation guidance](https://docs.speechmatics.com/speech-to-text/accuracy-benchmarking). These sources do not endorse this tool.

Original AI-assisted code and documentation by the PewTranslate project. Examples are synthetic English material, not recordings, actual ASR outputs, field trials or translations. PewTranslate's live-translation accounts remain closed. This utility works independently of those accounts.

Public files are `index.html`, `README.md` and `LICENSE`. Original material is MIT licensed, copyright 2026 szj2ys. Local `.verification/` files are development evidence and are not part of the publication.
