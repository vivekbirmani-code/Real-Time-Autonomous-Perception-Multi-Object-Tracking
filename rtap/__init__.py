# RTAP — Real-Time Autonomous Perception (AGPL-3.0)

__version__ = "8.4.121"

import importlib
import os
import sys
from typing import TYPE_CHECKING

# Set ENV variables (place before imports)
if not os.environ.get("OMP_NUM_THREADS"):
    os.environ["OMP_NUM_THREADS"] = "1"  # default for reduced CPU utilization during training

from rtap.utils import ASSETS, SETTINGS
from rtap.utils.checks import check_rtap as checks
from rtap.utils.downloads import download

settings = SETTINGS

MODELS = ("YOLO", "YOLOWorld", "YOLOE", "NAS", "SAM", "FastSAM", "RTDETR", "LLM")

__all__ = (  # noqa: PLE0604
    "__version__",
    "ASSETS",
    *MODELS,
    "checks",
    "download",
    "settings",
)

if TYPE_CHECKING:
    from rtap.models import LLM, YOLO, YOLOWorld, YOLOE, NAS, SAM, FastSAM, RTDETR  # noqa


def __getattr__(name: str):
    """Lazy-import public classes on first access."""
    if name in MODELS:
        return getattr(importlib.import_module("rtap.models"), name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__():
    """Extend dir() to include lazily available public names for IDE autocompletion."""
    return sorted(set(globals()) | set(MODELS))


if __name__ == "__main__":
    print(__version__)
