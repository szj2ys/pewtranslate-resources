# Caption display rehearsal

A standalone operator tool for rehearsing a short deck of your own reviewed caption text. Manually step through cues at fixed display settings, compare actual wrapping or clipping, and download an observation handoff. It does not create captions, translate, play media or run a live service.

Open `index.html` in a modern browser. There is no build, server, installation, account, external asset or network dependency. Optional reference links are ordinary external navigation.

## A real preparation workflow

1. Start a blank deck or load the clearly fictional English practice deck. Both workspace buttons explicitly clear cues, settings and observations; download anything you need first.
2. Enter your own reviewed wording, including explicit line breaks. Select **Apply cue text**. Pending edits hide the preview and must be applied or discarded before switching cues. Previewing and exporting never rewrite accepted text.
3. Choose a font size, line-height multiplier, requested box width/height and opaque text/background colors. Use automatic, left-to-right or right-to-left direction as appropriate. All typography uses the device’s system font.
4. Use **Previous cue**, **Next cue**, **Blank view** and **Restore cue**. These are standard keyboard-operable buttons. There are no timers, global shortcuts, automatic playback or fullscreen automation.
5. Record what you actually saw. Compare the same cue at two settings, or on the intended device. Each observation stores its own text, cue revision/order, settings, measured dimensions, visibility state and optional note. A blank observation is marked blank and never assessed as fitting. No note means no note, not approval.
6. Download the JSON handoff. It includes every observation, the current accepted deck and revision-level coverage. Check which cues still lack a visible observation. Ask intended readers about their needs; the app cannot establish that anyone was consulted.

## What the display measures

Font size is fixed in **CSS pixels**; it is never reduced to make text fit. The stage has a two-pixel border and 16-pixel padding. Requested width is capped by the available page width. The UI and snapshots show actual border-box, client, content and scroll dimensions, along with requested settings. A narrower viewport can change wrapping without changing font size.

Text retains line breaks and normal browser wrapping. An overlong unbroken token can overflow horizontally. The stage clips excess text, with a visible notice; the full uncut text remains in an expandable plain-text view. Horizontal/vertical overflow means the stage’s scroll dimension exceeds its client dimension by more than one CSS pixel, allowing for browser rounding. Measurements update after layout, font readiness, resizing and changes of cue/settings. Blank views retain geometry but their overflow results are `null` and `not-assessed-blank`.

“Fits this measured box” describes layout only. CSS pixels are not physical size. This is not a calibrated phone, projector or media-player simulator. It cannot test viewing distance, room lighting, visual needs, font availability, audience preference, audio synchronization, reading speed, meaning, accuracy or standards compliance. Colors are visual choices, not a numeric contrast certificate. Use the actual intended display and relevant human review.

## Limits and preservation

- At most 20 cues, 2,000 UTF-16 code units per accepted cue, and 12,000 across the accepted deck.
- At most 60 observations; each note may contain up to 1,000 UTF-16 units.
- Font size: whole CSS pixels from 16 to 96. Line height: multiplier from 1 to 2. Width: whole CSS pixels from 160 to 1,200. Height: whole CSS pixels from 80 to 800. Colors: opaque `#rrggbb` only.

Empty cues can remain as placeholders but cannot be displayed or recorded. Invalid settings pause the preview. Over-limit edits remain in the editor with an explicit rejection; accepted text is not truncated or overwritten. Applying a changed cue creates a new revision and marks it custom. Earlier snapshots keep their original text and provenance. Removing a cue does not erase its observations. Loading a deck or resetting clears the entire log explicitly. Ordinary navigation, text/settings edits and resizing do not mutate recorded snapshots.

A textarea may normalize pasted CRLF/CR line endings to LF. Exact text means the accepted current editor string, not unavailable original file bytes. No case folding, Unicode normalization or translation is applied. UTF-16 units are a browser string bound, not a count of letters or reading effort.

## Privacy and handoff

Everything is kept in page memory. Closing or refreshing loses the workspace. The page has no network requests, external scripts/fonts/images, analytics, cookies or persistent storage; a restrictive CSP blocks connections. No microphone, camera, audio/video, file upload or second-screen communication is used. Cue text and notes enter DOM text nodes, with bidirectional isolation from application labels.

The JSON download is data, not executable HTML or CSV. Native JSON escaping preserves accepted strings, including unusual control/code-unit sequences. It has a fixed filename and contains all observations, not just the current view. It records whether a pending edit was excluded and distinguishes missing notes and unobserved current revisions. No spreadsheet formula evaluation is introduced by the tool. Treat supplied wording and observations as potentially sensitive and share the file deliberately.

## Context and ownership

The [PewTranslate setup and rehearsal guide](https://pewtranslate.com/en/guides/set-up-live-translation-for-your-church) discusses testing the intended setup with competent human review. [W3C’s captions guidance](https://www.w3.org/WAI/media/av/captions/) explains the broader captioning task, including synchronization and relevant non-speech information. These sources do not endorse or validate this implementation.

This is an original AI-assisted resource by [PewTranslate](https://pewtranslate.com/). Live-translation accounts are closed; PewTranslate projector captions are not available. This standalone display rehearsal supplies neither service and makes no claim of production use, accessibility certification or translation accuracy.

Publish only `index.html`, `README.md` and `LICENSE`. The local `.verification/` folder is development evidence and must not be published. MIT license, copyright 2026 szj2ys.
