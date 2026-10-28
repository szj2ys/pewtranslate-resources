# Browser locale inspector

A standalone batch diagnostic for locale configuration. Paste one locale tag per line, inspect what the current browser does with it, and download a row-by-row CSV for a developer or localization reviewer. The tool keeps originals, blank rows and duplicate canonical mappings. It does not rewrite or deduplicate your list.

Open `index.html` directly in a modern browser. No server, install, account, storage, external assets or network connection is needed. Optional documentation links navigate externally only when followed.

## Workflow

1. Paste one tag per line, or load the example configuration. Its tags are public examples, not real user data or a product language list.
2. Enter the locale in which you want language labels, such as `en` or `fr`.
3. Select **Inspect this batch**. Read canonicalization, DateTimeFormat lookup and localized-name results separately. The result shows the actual resolved display locale, which may differ from your request.
4. Review the next action for each row. A canonical duplicate points to the first row with the same canonical identifier; both original rows remain.
5. Download **all rows CSV**. Results appear 100 rows at a time, with a button to show more; every inspected row is included in the export. Changing input or display settings clears stale results until another inspection.
6. Reset to blank or refresh to discard page memory. Keep your source list elsewhere if you need it later.

Leading and trailing whitespace is trimmed in a separate API input value. Original row text remains in the editor and CSV. A trailing newline creates a final blank row. The browser textarea normalizes line endings; CRLF, CR and LF are separators, not part of exported row values. Formula protection intentionally adds a prefix to some exported cells, as described below.

## Interpret the named checks

### Canonical identifiers

Each row independently calls `Intl.getCanonicalLocales([trimmedTag])`. “Accepted by Intl” means this browser accepted the structure and returned a canonical identifier. Case and historical aliases may change. “Rejected by Intl” identifies a `RangeError` from that API, not a definitive judgment on all BCP 47 forms, registration or whether a language exists. Unknown but structurally accepted identifiers can remain accepted. See [MDN’s canonicalization reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/getCanonicalLocales) and [ECMA-402](https://tc39.es/ecma402/).

### DateTimeFormat, lookup mode

`Intl.DateTimeFormat.supportedLocalesOf([canonical], {localeMatcher: 'lookup'})` tests whether this one service can match without the runtime’s default locale. A match may use a broader locale and does not prove exact dialect, region or extension data. A separately constructed formatter’s `resolvedOptions().locale` is shown, including the default-locale fallback result when there is no non-default match. This is neither all-Intl coverage nor translation support. Even an unchanged resolved identifier does not certify every extension’s behavior. See [DateTimeFormat matching](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/supportedLocalesOf).

### Localized display names

The query uses `new Intl.Locale(canonical).baseName`, which excludes extensions and private-use subtags while retaining the language, script, region and variants. That queried value is displayed. Names come from `Intl.DisplayNames` with `type: 'language'`, `languageDisplay: 'standard'`, `localeMatcher: 'lookup'` and `fallback: 'none'`. An `undefined` result becomes **No localized name returned**, not an invented label or a nonexistent-language claim.

The display-locale request is independently canonicalized. Its `DisplayNames.supportedLocalesOf` lookup and the instance’s actual `resolvedOptions().locale` are both reported. An unfamiliar display locale can use the runtime default. An invalid display setting leaves the other row checks available. References: [DisplayNames options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames), [name lookup](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of) and [Locale baseName](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/baseName).

Unavailable APIs, thrown exceptions and absent localized names are separate states. If `Intl.Locale` is unavailable, name queries are skipped because their base identifier could not be obtained. Browser versions, locale data and builds may differ. Run the batch in each runtime you actually need to support, then test the real interface. No registry, linguistic, accessibility, comprehension or product-coverage certification is performed.

## Limits, privacy and export

- At most 64 KiB of UTF-8 input and 1,000 rows. Larger batches are rejected in full; oversized clipboard pastes are not inserted.
- A trimmed row above 256 UTF-16 code units is retained and reported without an API call. The display-locale setting has a 128-code-unit limit. These are practical tool bounds, not language-tag standards.
- Processing runs in memory, yields between small groups of rows and can be cancelled by resetting or editing the input. No cookies, local storage, analytics, remote fonts or requests are used. Imported text is inserted with DOM text APIs, never interpreted as markup. A restrictive content security policy blocks external resources and connections.
- CSV uses quoted fields, doubled internal quotes, CRLF records and a UTF-8 BOM. Fields starting with `=`, `+`, `-` or `@`, including after leading whitespace/control characters, receive a leading apostrophe. A leading tab or line break is also protected. Keep these prefixes when importing untrusted values into spreadsheets.
- The 19 CSV columns include row number, original/API input, canonicalization state and identifier, duplicate reference, named DateTimeFormat results, base-name query, localized label state, requested/canonical/resolved display locales, display-setting state, next actions and observation time. The timestamp records an observation of this runtime, not universal language support. No raw browser fingerprint or user agent is included in the export.

## A language selector still needs people

An identifier is not a person’s language preference. If this configuration will become a language selector, ask intended readers to review recognizable labels and the actual content. [PewTranslate’s welcoming multilingual visitors guide](https://pewtranslate.com/en/guides/welcoming-multilingual-visitors) discusses offering choices without guessing someone’s language. This reference provides human context; its product language list is not evidence about browser APIs.

AI-assisted code, published by [PewTranslate](https://pewtranslate.com/). Live-translation accounts are closed. This local diagnostic neither translates nor verifies PewTranslate language coverage or production availability.

## Publication files

Only `index.html` and `README.md` are public candidates. Exclude `.verification/`, which holds local checks, captures and implementation evidence. There is no build step or dependency.

## License

MIT License

Copyright (c) 2026 szj2ys

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
