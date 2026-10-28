# Subtitle timing and readability checker

A small local tool for turning an SRT or WebVTT subtitle file into an actionable review list. It helps a person locate timing problems and cues that exceed their own line-length or reading-rate preferences. It does not translate, repair subtitles, judge meaning, or certify a subtitle standard or accessibility requirement.

Open `index.html` in a modern browser. No server, installation, account or internet connection is needed. The reference links are optional external navigation.

## A useful review workflow

1. Keep your original subtitle file. Open a UTF-8 `.srt` or `.vtt` copy in the tool, or paste its text. The fictional English demo is available for practice.
2. Choose a maximum number of characters per line and per second. The initial values of 42 and 20 are editable starting preferences, not rules for every language or audience. Turn overlap flags off when they are not useful to your workflow.
3. Select **Review subtitles**. Resolve errors and unsupported features first. They make the review incomplete, even when other cues can be inspected.
4. Use each issue’s source line, cue identifier and timestamps to find it in your subtitle editor. The suggestion explains a possible next action; check it against the recording before changing anything.
5. Download the complete issue CSV for a review handoff, or print the displayed issue list. Editing text or settings invalidates old results until you run the review again. Clear or refresh the page to discard page memory.

The tool never writes back to your file or changes the editor text during analysis. Parsing uses a separate copy with line endings normalized; a browser textarea may display imported CRLF/CR line endings as LF. File bytes on disk are untouched. No corrected-subtitle export is offered.

## Supported subset and explicit limitations

**SRT:** blank-line-separated blocks, each containing a numeric index, one `HH:MM:SS,mmm --> HH:MM:SS,mmm` timing line, and plain text. Hours need at least two digits; minutes and seconds must be 00–59. Commas and exactly three millisecond digits are required. Missing numeric indices are reported even if timing can be recovered.

**WebVTT:** a first-line `WEBVTT` header, a blank line, then plain-text cues with optional single-line identifiers. Timings use `MM:SS.mmm` or `HH:MM:SS.mmm` with exactly three millisecond digits. An optional UTF-8 BOM and CRLF, CR or LF line endings are accepted. NOTE blocks are counted and skipped; a timing arrow in a NOTE block is flagged because it may hide a missing separator.

This is deliberately not a complete WebVTT validator. STYLE and REGION blocks, header metadata, cue settings, markup, entities and embedded timestamps are reported as unsupported. Unsupported does not mean the source is invalid. Marked-up text and cues with another timing arrow in the payload do not receive text metrics. Their supported positive time intervals can still receive overlap/order flags. Settings are not applied to layout. See the [W3C WebVTT specification](https://www.w3.org/TR/webvtt1/) for the full format, including legitimate overlapping cues and styled payloads.

Malformed blocks, invalid timestamps, absent text, nonpositive durations, replacement/control characters and missing separators produce visible issues. Auto-detection treats a `WEBVTT` header as WebVTT and other input as SRT; dot-separated timings without a header produce an error. Choose WebVTT explicitly to inspect such a damaged file without pretending its header is valid. Missing separators without an embedded timing arrow may be indistinguishable from ordinary caption text; always check playback.

Line length and reading rate count **Unicode code points**, including spaces and punctuation but excluding line breaks. They do not measure rendered width, perceived letters, words or actual reading comprehension. Combining marks and multi-code-point emoji count separately. Reading rate is the character count divided by cue duration. Overlap flags identify one active overlapping cue for each later cue; they do not enumerate every pair in a dense overlap. Out-of-order starts are review flags. These observations are prompts for a person, not universal errors.

Input is bounded at **2 MiB of UTF-8 text, 5,000 blank-line-separated blocks and 30,000 lines**. A file above any bound is rejected rather than partly reported as clean. The screen and print view show at most 200 issue rows; the CSV contains every issue from the accepted input. The full cue text is retained in CSV even when the on-screen excerpt is shortened. There is no media player, live timing sync, spelling check, translation, rich-text rendering or automatic repair.

## Privacy and CSV handling

All processing stays in page memory. There are no external scripts, fonts, analytics, cookies, storage calls or automatic network requests. Imported text is inserted as plain DOM text, never executed as HTML. A restrictive content security policy blocks network connections and external resources. Optional reference links leave the tool only when you follow them.

The CSV has eight columns: category, cue, source line, start, end, issue, suggested next action and original cue text. It uses quoted fields, doubled quotes, CRLF row endings and a UTF-8 BOM. Formula-like fields beginning with `=`, `+`, `-` or `@`, including those after leading whitespace/control characters, receive a leading apostrophe. Cells beginning with a tab or line break also receive an apostrophe. This intentionally alters those export cells to reduce spreadsheet formula risk; it does not change source input. Spreadsheet import behavior varies, so keep the downloaded file with your review notes and do not remove its protective prefixes when opening untrusted text.

## Review meaning as well as timing

The relevant [PewTranslate guide to checking sermon transcript and translation errors](https://pewtranslate.com/en/guides/check-sermon-transcript-translation-errors) explains how to record uncertain wording, consult the speaker and involve a competent language reviewer. Timing checks cannot verify names, meaning, speaker identification or relevant sounds. Ask the intended audience whether the captions are useful.

This is an AI-assisted resource by [PewTranslate](https://pewtranslate.com/). Live-translation accounts are closed. The standalone checker does not connect to that service and supplies no claim of translation accuracy or production use.

## Publication files

Publish `index.html` and this `README.md`. The local `.verification/` directory contains development checks and captures; exclude it from publication. The two public files have no build step or dependency.

## License

MIT License

Copyright (c) 2026 szj2ys

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
