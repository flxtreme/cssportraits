# Instructions

## Project Summary
This workspace is for generating CSS-only portraits with an accompanying QR code. Inputs live under `files/`, and outputs are written under `portraits/`.

## Inputs
- Each portrait has a folder under `files/<subject>/`.
- The file `files/<subject>/message.md` uses this format:
  - `# Name` on its own line, followed by the name on the next line.
  - `# Message` on its own line, followed by the full message text.
  - Optional `# Loop` on its own line, followed by `N Times` to indicate repetition count.

## Outputs
- Generate `portraits/<subject>/index.html`.
- Each output folder must include 4 files:
  - `index.html` with a download button for `postcard.png`.
  - `image.png` copied from `files/<subject>/image.png`.
  - `postcard.png` (a rendered image of the postcard).
  - `qr.png` that links to the generated portrait page (generate with `genearateqr.py`).

## Generation Rules
- Read all `files/*/message.md` entries.
- Skip subjects that already have `portraits/<subject>/index.html`.
- Do not overwrite or update existing generated files unless explicitly requested.
- Do not modify templates or generator scripts during generation unless explicitly requested.
- For each subject:
  1. Extract the requirements and visual cues from the message.
  2. If `# Loop` is present, duplicate the `# Message` text `N` times.
  3. Use the full `# Message` text as-is, including any repeated/duplicated content.
  4. Use the value under `# Name` for the name label. If missing, fall back to the subject folder name.
  5. Set the HTML `<title>` to `{Name} Portrait`, using the `# Name` value or the subject folder name.
  6. Produce a self-contained `index.html` with embedded CSS and a download button for `postcard.png`.
  7. Copy `files/<subject>/image.png` into `portraits/<subject>/image.png`.
  8. Always run `genearateqr.py` to create `portraits/<subject>/qr.png` that points to the portrait URL (do not prompt).
  9. Always run `generatepostcard.py` to create `portraits/<subject>/postcard.png` from the postcard element (do not prompt).
  10. Do not include the QR code anywhere in the HTML output; it should not appear on the page.

## Prompt Template
Use this as the prompt for each subject:

"""
You are generating a CSS-only portrait page.

Input message:
{message.md contents}

Requirements:
- Create `portraits/{subject}/index.html`.
- The portrait must be drawn using HTML + CSS only (no external images).
- Do not include a QR code in the HTML; `qr.png` is generated as a standalone file only.
- Keep everything self-contained in a single HTML file with embedded CSS.
- Add a download button that points to `postcard.png`.
- If `# Loop` is present, duplicate the `# Message` text `N` times.
- Use the full `# Message` text as-is, including any repeated content.
- Use `# Name` from `message.md` for the label, or fall back to the subject name.
- Set the HTML `<title>` to `{Name} Portrait` using the same `# Name` value or fallback.
- Do not place a QR in the HTML at all.

Output only the full HTML for index.html.
"""
