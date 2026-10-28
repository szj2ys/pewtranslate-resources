# Multilingual welcome sign builder

A standalone, account-free tool for making one A4 welcome sign from your own reviewed wording.

Open `index.html` in a modern browser. No install, server, external assets, account, or network connection is required for the builder. The reference links are optional external navigation.

1. Enter a title, an optional subtitle, and up to three language lines.
2. Choose automatic, left-to-right, or right-to-left reading direction for the headings and each line. Choose portrait or landscape A4 and centered or direction-relative alignment.
3. Ask competent speakers to review the wording and check what assistance the sign promises. The review checkbox records the user's judgment, not verification by the app.
4. Print, save as PDF through the native print dialog, or download an HTML copy. Use A4, disable browser headers/footers, and inspect the preview. Check the physical result at its intended viewing distance.

The title is limited to 60 characters, subtitle to 100, and each language line to 120. The layout reduces text size when necessary and prevents export when text still overflows. Short wording is easier to read. System fonts determine script coverage; use a font installed on the printing device that supports the entered language.

The fictional demo contains English only and keeps its example label in printed/exported output. Clear it before creating a real sign. No translations, accuracy guarantees, user testimonials, or ministry outcomes are supplied. AI-assisted implementation; human language review is still required.

## Privacy and output

Entries remain in page memory. There is no local storage, cookie, analytics, telemetry, remote font, or network request. Refreshing or closing the builder discards the editor state. The downloaded HTML keeps the rendered sign, not an editable form. It is self-contained and includes a restrictive content security policy with scripts and network resources disabled. User wording is inserted with `textContent`; exported title text is escaped, and the sign is serialized from DOM text nodes.

The downloaded HTML uses A4 page rules and retains per-line direction. A native browser print dialog still controls printer settings. A reader can reopen the export offline and print it with the browser's command. No SVG export is supplied: HTML better preserves ordinary browser shaping and wrapping across different writing systems.

## References

- [Welcoming multilingual visitors](https://pewtranslate.com/en/guides/welcoming-multilingual-visitors): practical context for signs, greeters, and follow-up. Confirm actual support before adapting a suggested message.
- [Census language lookup by ZIP code](https://pewtranslate.com/en/guides/languages-spoken-by-zip-code): area-level home-language estimates, not individual preferences.

PewTranslate live-translation accounts remain closed. This tool has no dependency on that software and does not advertise unavailable interpretation.

## Tested behavior and limitations

Checked in Chromium on 28 October 2026 at desktop (1280 px) and mobile (390 px) widths: 23 functional checks passed. These covered the review gate, independent text directions, literal handling of HTML-like wording, long-text fitting, offline HTML download and reopening, single-page A4 portrait/landscape output, and clearing entries on refresh. No external requests or JavaScript runtime errors were observed. The mobile layout had no horizontal overflow.

The builder is designed for modern browsers with CSS container-query units. Native printer settings, system font coverage, and text legibility still need a check on your own device. A checkbox cannot verify language accuracy or whether the promised welcome assistance exists.

## License

MIT License

Copyright (c) 2026 szj2ys

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
