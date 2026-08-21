"""Download demo image and video for local tracking smoke tests."""

from pathlib import Path

from rtap.utils.downloads import download

ASSETS = Path(__file__).resolve().parents[1] / "rtap" / "assets"
# Public sample media used for local smoke tests (override with RTAP_ASSETS_URL if needed).
DEMO_URLS = [
    "https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg",
]


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    download(DEMO_URLS, dir=ASSETS)
    demo_image = ASSETS / "bus.jpg"
    downloaded = ASSETS / Path(DEMO_URLS[0]).name
    if downloaded.is_file() and not demo_image.is_file():
        downloaded.rename(demo_image)
    for path in (demo_image,):
        status = "OK" if path.is_file() else "MISSING"
        print(f"{status}: {path}")


if __name__ == "__main__":
    main()
