# RTAP — Real-Time Autonomous Perception (AGPL-3.0)

from .fastsam import FastSAM
from .llm import LLM
from .nas import NAS
from .rtdetr import RTDETR
from .yolo import YOLO, YOLOE, YOLOWorld

__all__ = "LLM", "NAS", "RTDETR", "SAM", "YOLO", "YOLOE", "FastSAM", "YOLOWorld"  # allow simpler import


def __getattr__(name):
    """Lazy-import SAM so standard YOLO imports don't load optional torchvision internals."""
    if name == "SAM":
        # Scoped for import rtap speed: SAM pulls optional torchvision-heavy modules.
        from .sam import SAM

        return SAM
    raise AttributeError(f"module {__name__} has no attribute {name}")
