# Text Mask Portrait Instructions

## Goal
Create a simple CSS portrait by using an image as the background, converting it to black and white, and blending it with a text layer so the image appears formed by the text.

## Input
- `files/<subject>/message.md` with this format:
	- `# Name` heading, followed by the name on the next line.
	- `# Message` heading, followed by the full message text.
	- Optional `# Loop` heading, followed by `N Times` to repeat the message.
- `files/<subject>/image.png`: the source image.

## Output
- `portraits/<subject>/index.html` (self-contained HTML + CSS).
- `portraits/<subject>/image.png` (copied from `files/<subject>/image.png`).
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
- If `# Loop` is present, duplicate the `# Message` text `N` times.
- Use the full `# Message` text as-is, even if it is duplicated.
- Use the value under `# Name` for the label; otherwise use the subject name.
- Do not include a QR code in the HTML at all; `qr.png` is a standalone file.

## Implementation Notes
- Use CSS filters (grayscale + contrast) on the background image.
- Use `mix-blend-mode` or `background-clip: text` to merge text with the image.
- The final result should be readable and clearly shows the face emerging from the text.
- Always generate `qr.png` and `postcard.png` without prompting.
