# Text Mask Portrait Instructions

## Goal
Create a simple CSS portrait by using an image as the background, converting it to black and white, and blending it with a text layer so the image appears formed by the text.

## Input
- `files/<subject>/message.md` with this format:
	- `# Name` heading, followed by the name on the next line.
	- `# Description` heading, followed by the text used for the CSS portrait.
	- `# Message` heading, followed by the text shown below the postcard label.
	- Optional `# Long Message` heading, followed by a longer letter/poem to show in the postcard body.
	- Optional `# Loop` heading, followed by `N Times` to repeat the description text.
	- Optional `# Theme` heading, followed by a theme name that maps to `template/<theme>.html`.
- `files/<subject>/image.*`: the source image (PNG, JPEG, JPG, or other supported format).

## Output
- `portraits/<subject>/index.html` (self-contained HTML + CSS).
- `portraits/<subject>/image.*` (copied from `files/<subject>/image.*` with same format).
- `portraits/<subject>/postcard.png` (rendered postcard image).
- `portraits/<subject>/qr.png` (QR code for the portrait URL).
 - Do not overwrite or update existing generated files unless explicitly requested.
- Do not modify templates or generator scripts during generation unless explicitly requested.

## Required Effect
- The image is the background.
- Apply a black-and-white filter to the image.
- The message text sits on top.
- Use a blend/filter effect so the image looks like it is created by the text.
- Add a download button in the page that links to `postcard.png`.
- If `# Theme` is present, use `template/<theme>.html` as the base template; otherwise use `template/valentines.html`.
- If `# Loop` is present, duplicate the `# Description` text `N` times.
- Use the full `# Description` text as-is, even if it is duplicated.
- Use the value under `# Message` as the label text below the portrait or postcard label.
- If `# Long Message` is present, render it as the postcard body text (a longer note below the label).
- Use the value under `# Name` for the label; otherwise use the subject name.
- Set the HTML `<title>` to `{Name} Portrait` using the same `# Name` value or fallback.
- Do not include a QR code in the HTML at all; `qr.png` is a standalone file.

## Implementation Notes
- Use CSS filters (grayscale + contrast) on the background image.
- Use `mix-blend-mode` or `background-clip: text` to merge text with the image.
- The final result should be readable and clearly shows the face emerging from the text.
- Always generate `qr.png` and `postcard.png` without prompting.
