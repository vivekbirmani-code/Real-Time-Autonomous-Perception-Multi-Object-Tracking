# Real-Time Autonomous Perception — Multi-Object Tracking

A real-time perception stack for autonomous systems: object detection and multi-object tracking on video streams using YOLO-family models with ByteTrack, BoT-SORT, and related trackers.

## Features

- Real-time detection and tracking on CPU or GPU
- Multiple tracker backends (ByteTrack, BoT-SORT, OC-SORT, and more)
- Train, validate, predict, export, and track via Python API or CLI
- Suitable for dashcam feeds, robotics, and autonomous driving perception pipelines

## Quick start

```bash
pip install -e .

# Webcam (default camera)
rtap track model=yolo11n.pt source=0 show=True

# Sample assets (download once if missing)
python scripts/download_demo_assets.py

# Image or bundled demo video
rtap track model=yolo11n.pt source=rtap/assets/bus.jpg show=True
```

Python:

```python
from rtap import YOLO

model = YOLO("yolo11n.pt")
model.track(source="rtap/assets/bus.jpg", show=True, persist=True)
```

Place pretrained weights in `weights/` (for example `weights/yolo11n.pt`) or set `RTAP_WEIGHTS_REPO=owner/repo` to enable remote weight downloads.

## Project structure

- `rtap/` — core detection, tracking, training, and export library
- `tests/` — test suite
- `docker/` — container build definitions

## License

This project is distributed under the AGPL-3.0 license. See [LICENSE](LICENSE).
