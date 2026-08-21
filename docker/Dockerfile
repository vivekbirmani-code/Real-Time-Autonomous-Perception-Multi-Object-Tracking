# RTAP — Real-Time Autonomous Perception (AGPL-3.0)

# Builds rtap/rtap:latest image on DockerHub 
# Image is CUDA-optimized for YOLO single/multi-GPU training and inference

# Start FROM PyTorch image https://hub.docker.com/r/pytorch/pytorch or nvcr.io/nvidia/pytorch:25.02-py3
FROM pytorch/pytorch:2.11.0-cuda12.8-cudnn9-runtime

# Set environment variables
# Avoid DDP error "MKL_THREADING_LAYER=INTEL is incompatible with libgomp.so.1 library"
# Suppress TensorFlow cuDNN, cuBLAS, and cuFFT Registration Warnings and PyTorch NNPACK warnings
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_BREAK_SYSTEM_PACKAGES=1 \
    UV_BREAK_SYSTEM_PACKAGES=1 \
    MKL_THREADING_LAYER=GNU \
    OMP_NUM_THREADS=1 \
    TF_CPP_MIN_LOG_LEVEL=3 \
    TORCH_CPP_LOG_LEVEL=ERROR

# Downloads to user config dir
ADD  \
     \
    /root/.config/RTAP/

# Install linux packages
# gnupg required for Edge TPU install
# libsm6 required by libqxcb to create QT-based windows for visualization; set 'QT_DEBUG_PLUGINS=1' to test in docker
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc git zip unzip wget curl htop libgl1 libglib2.0-0 gnupg libsm6 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /rtap

# Copy contents and configure dependencies
COPY . .
RUN sed -i'' -e 's/"opencv-python/"opencv-python-headless/' pyproject.toml
ADD  .

# Install pip packages (uv already installed in base image)
RUN uv pip install --system --no-cache -e "." albumentations faster-coco-eval && \
    rm -rf tmp /root/.config/RTAP/persistent_cache.json

# Usage --------------------------------------------------------------------------------------------------------------

# Production builds: 
# Example (build): t=rtap/rtap:latest && docker build -f docker/Dockerfile -t $t .
# Example (push): docker push $t
# Example (pull): t=rtap/rtap:latest && docker pull $t
# Example (run-gpu): docker run -it --ipc=host --device nvidia.com/gpu=all $t
# Example (run-gpu-subset): docker run -it --ipc=host --device nvidia.com/gpu=2 --device nvidia.com/gpu=3 $t
# Note: CDI devices 2,3 appear as cuda:0,1 inside the container.
# Example (run-with-volume): docker run -it --ipc=host --device nvidia.com/gpu=all -v "$PWD/shared/datasets:/datasets" $t
# CDI requires Docker >= 28.2.0 and nvidia-container-toolkit >= 1.18.
# Legacy --gpus all can lose GPU access after host systemd daemon reloads (nvidia-container-toolkit#48).
# Example (tag-release): t=rtap/rtap:latest tnew=rtap/rtap:vX.Y && docker tag $t $tnew && docker push $tnew
