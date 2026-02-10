import asyncio
from pathlib import Path

from pyppeteer import launch

ROOT = Path(__file__).resolve().parent
FILES_DIR = ROOT / "files"
PORTRAITS_DIR = ROOT / "portraits"
SELECTOR = ".postcard"


POSTCARD_WIDTH_IN = 4
POSTCARD_HEIGHT_IN = 6
CSS_DPI = 96
OUTPUT_DPI = 300
POSTCARD_TEXT_FONT = "clamp(8px, 0.5vw, 14px)"


async def save_postcard_as_png(page, html_file: Path, selector: str, output_file: Path) -> None:
    html_path = html_file.resolve()
    await page.goto(html_path.as_uri())
    await page.waitForSelector(selector)

    # Override text size and hide UI for postcard output only.
    await page.addStyleTag(
        {
            "content": (
                f".text-portrait {{ font-size: {POSTCARD_TEXT_FONT} !important; }}"
                ".controls, .download-btn { display: none !important; }"
            ),
        }
    )

    element = await page.querySelector(selector)
    await element.screenshot({"path": str(output_file)})
    print(f"Saved '{selector}' as '{output_file}'")


async def main() -> None:
    if not FILES_DIR.exists():
        raise SystemExit(f"Missing files directory: {FILES_DIR}")

    subjects = [
        path for path in sorted(FILES_DIR.iterdir()) if path.is_dir() and (path / "message.md").exists()
    ]

    if not subjects:
        raise SystemExit("No subjects found in files/.")

    browser = await launch(headless=True)
    page = await browser.newPage()

    css_width = int(POSTCARD_WIDTH_IN * CSS_DPI)
    css_height = int(POSTCARD_HEIGHT_IN * CSS_DPI)
    device_scale = OUTPUT_DPI / CSS_DPI
    await page.setViewport(
        {"width": css_width, "height": css_height, "deviceScaleFactor": device_scale}
    )
    await page.emulateMedia("screen")

    for subject_dir in subjects:
        subject = subject_dir.name
        output_dir = PORTRAITS_DIR / subject
        index_path = output_dir / "index.html"

        if not index_path.exists():
            print(f"Skipping {subject}: missing {index_path}")
            continue

        output_file = output_dir / "postcard.png"
        await save_postcard_as_png(page, index_path, SELECTOR, output_file)

    await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
