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

# Download weights and run tracking on a video or webcam
yolo track model=yolo11n.pt source=0 show=True
```

Python:

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
model.track(source="video.mp4", show=True, persist=True)
```

## Project structure

- `ultralytics/` — core detection, tracking, training, and export library
- `tests/` — test suite
- `docker/` — container build definitions

## License

This project is distributed under the AGPL-3.0 license. See [LICENSE](LICENSE).
