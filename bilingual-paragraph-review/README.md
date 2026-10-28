# Bilingual paragraph review

A local workspace for a human to associate blocks from an original excerpt and a supplied translation, retain questions against a fixed revision, and download a complete handoff. It does not translate, infer meaning, score quality or approve wording.

Open `index.html` in a modern browser with JavaScript and Web Crypto SHA-256 available. No server, account, package or installation is needed. Processing stays in page memory; refresh discards it. Download JSON to keep a reopenable copy.

## Use the workspace

1. Enter both supplied excerpts or load the clearly labelled fictional English layout example. The example is not a translation. Optional language labels are user assertions. Each side has an independent display direction.
2. Preview the blocks and exact ranges, then freeze the revision. All blocks start unassigned.
3. Select one or more source and target blocks and create an association. Multi-block and reordered relationships are allowed. A block can belong to only one active group. Unlink explicitly before reassigning.
4. Add group or block notes and a human-entered state. Valid notes are kept in memory as typed. Oversized notes block other operations and exports until corrected; the last valid value is retained internally. “Operator marked checked” records an assertion, not verified competence or system approval.
5. Read the unassigned blocks and their notes. No counterpart recorded does not mean an omission, addition or error. Fully assigned text is not evidence of correct translation.
6. Download the JSON and readable HTML. They contain both complete supplied texts, exact block/separator ranges, every association and note, and the unassigned IDs. Share deliberately.
7. To continue, open a fresh copy of the workspace and paste the complete JSON into **Reopen a saved JSON snapshot**. Validation completes before replacement. Cancelled replacement and invalid snapshots keep the current session.

Frozen texts cannot be edited in place. **Start a new revision** offers a cancellation point and reminds you to export. It keeps the text in the draft but clears all groups and notes. Old judgments never transfer automatically, even when paragraphs look identical. Removed group notes are discarded only after confirmation; block notes remain attached to their original blocks. This is a current snapshot, not an immutable audit history or a signed reviewer record.

## Exact text and segmentation

The `blank-lines-v1` rule treats `LF [SPACE|TAB]* LF` plus any further `[SPACE|TAB]* LF` repetitions as a separator. Every nonempty intervening piece is a block, including its leading/trailing whitespace and single line breaks. Leading/trailing separators remain recorded. This is a layout rule, not linguistic sentence or paragraph segmentation. Both sides need non-whitespace text.

Ranges are zero-based UTF-16 `[start,end)` positions in accepted browser textarea values. Browsers may turn CRLF/CR into LF before the page receives the value; original file bytes and pre-paste line endings are not retained. No Unicode normalization or trimming is applied to accepted text. Imported document/note strings must use LF line endings, matching accepted textarea values; CR is rejected rather than converted. Imported language labels must be single-line, matching the text inputs. Repeated equal blocks have distinct positional IDs within their revision.

Unpaired surrogate units and selected controls are rendered as visible `\uXXXX` escapes in previews and HTML. A supplementary surrogate pair remains its original character. Exact escaped values and ASCII-escaped JSON preserve every accepted code unit; display escapes alone are not the authoritative representation. User text is inert and isolated from interface labels. No URLs from supplied text become links or image requests.

Revision identity combines a random ID, capture timestamp and SHA-256 of an explicitly serialized version/rule/ID/time/text/label/direction tuple. The digest is a consistency check, not a signature or proof of identity. Imports also independently regenerate all block/separator ranges and validate every ID, group, note and unassigned set. Recomputing a digest cannot make forged ranges pass. Someone deliberately editing an entire consistent snapshot can create another record; no tamper-proof history is claimed.

## Bounds and format

- Each document: 20,000 UTF-16 units, at most 80 blocks.
- Active associations: at most 80; each needs at least one block on both sides.
- Each block/group note: 1,000 UTF-16 units. Each optional language label: 80 units.
- Pasted JSON: at most 2 MiB UTF-8, checked before parsing. Excess is rejected, not truncated.

JSON format `pewtranslate-manual-paragraph-review`, version `1`, includes `revision`, `documents`, `groups`, `blockNotes`, `unassigned`, `segmentation` and `exportedAt`. Unknown fields/versions, mismatched source ranges, duplicate/unknown IDs, duplicate group membership, cross-revision notes, invalid states and inconsistent coverage are rejected before session replacement. Validated values are copied into the internal structure; imported objects are never evaluated or merged into application settings.

The downloaded HTML has no scripts or external assets and opens offline as a reading copy. Its complete texts, relationships and unassigned blocks are visible; expandable escaped values preserve diagnostic detail. JSON is the format for reopening. There is no file-import picker dependency.

## Privacy and context

No application network requests, analytics, external assets, cookies, automatic storage, microphone or remote review. The page uses a restrictive content security policy. Reference links leave the page only when activated. Local processing is not a legal confidentiality guarantee; avoid sensitive examples and share exports deliberately.

The [PewTranslate transcript and translation review guide](https://pewtranslate.com/en/guides/check-sermon-transcript-translation-errors) explains human follow-up. A competent language reviewer must assess meaning in context. This workspace organizes supplied evidence, without linguistic certification or a global readiness decision.

Original AI-assisted code and documentation by the PewTranslate project. All supplied examples are fictional English layout material, not translations, recordings, field trials or third-party endorsements. PewTranslate's live-translation accounts remain closed. Original material is MIT licensed, copyright 2026 szj2ys.

Public files: `index.html`, `README.md`, `LICENSE`. Local `.verification/` files are not part of the publication.
