"""Download demo image and video for local tracking smoke tests."""

from pathlib import Path

from ultralytics.utils.downloads import download

ASSETS = Path(__file__).resolve().parents[1] / "ultralytics" / "assets"
DEMO_URLS = [
    "https://github.com/ultralytics/assets/releases/download/v0.0.0/bus.jpg",
    "https://github.com/ultralytics/assets/releases/download/v0.0.0/solutions_ci_demo.mp4",
]


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    download(DEMO_URLS, dir=ASSETS)
    for url in DEMO_URLS:
        path = ASSETS / Path(url).name
        status = "OK" if path.is_file() else "MISSING"
        print(f"{status}: {path}")


if __name__ == "__main__":
    main()
