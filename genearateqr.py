"""Generate QR codes for each subject in files/."""

# Install dependency:
# pip install qrcode[pil]

from pathlib import Path

import qrcode

ROOT = Path(__file__).resolve().parent
FILES_DIR = ROOT / "files"
PORTRAITS_DIR = ROOT / "portraits"
URL_TEMPLATE = "https://flxtreme.github.io/cssportraits/portraits/{subject}/index.html"


def generate_qr(url: str, output_path: Path) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)


def main() -> None:
    if not FILES_DIR.exists():
        raise SystemExit(f"Missing files directory: {FILES_DIR}")

    subjects = [
        path for path in sorted(FILES_DIR.iterdir()) if path.is_dir() and (path / "message.md").exists()
    ]

    if not subjects:
        raise SystemExit("No subjects found in files/.")

    for subject_dir in subjects:
        subject = subject_dir.name
        output_dir = PORTRAITS_DIR / subject
        output_dir.mkdir(parents=True, exist_ok=True)

        url = URL_TEMPLATE.format(subject=subject)
        output_path = output_dir / "qr.png"
        generate_qr(url, output_path)
        print(f"Generated {output_path} -> {url}")


if __name__ == "__main__":
    main()
