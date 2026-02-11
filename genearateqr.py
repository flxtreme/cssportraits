"""Generate QR codes for each subject in files/."""

# Install dependency:
# pip install qrcode[pil]

from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FILES_DIR = ROOT / "files"
PORTRAITS_DIR = ROOT / "portraits"
URL_TEMPLATE = "https://flxtreme.github.io/cssportraits/portraits/{subject}/index.html"


def generate_qr(url: str, output_path: Path) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Generate QR code with pink color
    qr_img = qr.make_image(fill_color="#cc3366", back_color="white").convert("RGB")
    qr_width, qr_height = qr_img.size
    
    # Create larger canvas for text on top
    text_height = 60
    total_height = qr_height + text_height
    canvas = Image.new("RGB", (qr_width, total_height), "white")
    
    # Draw "SCAN ME" text on top
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
    except:
        font = ImageFont.load_default()
    
    text = "SCAN ME"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (qr_width - text_width) // 2
    text_y = 35
    draw.text((text_x, text_y), text, fill="#cc3366", font=font)
    
    # Paste QR code below text
    canvas.paste(qr_img, (0, text_height))
    
    # Add heart icon in center of QR code
    heart_size = 60
    heart_emoji = Image.new("RGBA", (heart_size, heart_size), (255, 255, 255, 0))
    heart_draw = ImageDraw.Draw(heart_emoji)
    
    # Draw heart shape
    heart_color = "#ff6f9a"
    # Heart as a simple shape using polygon
    heart_points = [
        (30, 15), (35, 10), (40, 8), (45, 10), (50, 15),
        (50, 20), (30, 45), (10, 20), (10, 15),
        (15, 10), (20, 8), (25, 10), (30, 15)
    ]
    heart_draw.polygon(heart_points, fill=heart_color)
    
    # Create white background circle for heart
    heart_bg = Image.new("RGB", (heart_size, heart_size), "white")
    heart_bg_draw = ImageDraw.Draw(heart_bg)
    heart_bg_draw.ellipse([5, 5, heart_size-5, heart_size-5], fill="white")
    
    # Composite heart on background
    heart_bg.paste(heart_emoji, (0, 0), heart_emoji)
    
    # Calculate center position in QR code area
    center_x = (qr_width - heart_size) // 2
    center_y = text_height + (qr_height - heart_size) // 2
    
    canvas.paste(heart_bg, (center_x, center_y))
    
    canvas.save(output_path)


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
