# Use the official Ubuntu image as a parent image
FROM ubuntu:20.04

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install software-properties-common
RUN apt-get update && \
    apt-get install -y software-properties-common

# Add deadsnakes PPA and install Python 3.10
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-distutils python3.10-venv

# Install pip using Python 3.10
RUN python3.10 -m ensurepip && \
    python3.10 -m pip install --upgrade pip setuptools wheel

# Upgrade pip and install the required Python packages
RUN python3.10 -m pip install --default-timeout=1000 filelock
RUN python3.10 -m pip install --default-timeout=1000 fsspec
RUN python3.10 -m pip install --default-timeout=1000 huggingface-hub
RUN python3.10 -m pip install --default-timeout=1000 jinja2
RUN python3.10 -m pip install --default-timeout=1000 networkx
RUN python3.10 -m pip install --default-timeout=1000 numpy
RUN python3.10 -m pip install --default-timeout=1000 nvidia-cublas-cu12==12.1.3.1
RUN python3.10 -m pip install --default-timeout=1000 nvidia-cuda-cupti-cu12==12.1.105
RUN python3.10 -m pip install --default-timeout=1000 nvidia-cuda-nvrtc-cu12==12.1.105
RUN python3.10 -m pip install --default-timeout=1000 nvidia-cuda-runtime-cu12==12.1.105
RUN python3.10 -m pip install --default-timeout=1000 nvidia-cudnn-cu12==8.9.2.26
RUN python3.10 -m pip install --default-timeout=1000 nvidia-cufft-cu12==11.0.2.54
RUN python3.10 -m pip install --default-timeout=1000 nvidia-curand-cu12==10.3.2.106
RUN python3.10 -m pip install --default-timeout=1000 nvidia-cusolver-cu12==11.4.5.107
RUN python3.10 -m pip install --default-timeout=1000 nvidia-cusparse-cu12==12.1.0.106
RUN python3.10 -m pip install --default-timeout=1000 nvidia-nccl-cu12==2.18.1
RUN python3.10 -m pip install --default-timeout=1000 nvidia-nvtx-cu12==12.1.105
RUN python3.10 -m pip install --default-timeout=1000 packaging
RUN python3.10 -m pip install --default-timeout=1000 pyyaml
RUN python3.10 -m pip install --default-timeout=1000 regex
RUN python3.10 -m pip install --default-timeout=1000 requests
RUN python3.10 -m pip install --default-timeout=1000 safetensors
RUN python3.10 -m pip install --default-timeout=1000 sympy
RUN python3.10 -m pip install --default-timeout=1000 tokenizers
RUN python3.10 -m pip install --default-timeout=1000 triton
RUN python3.10 -m pip install --default-timeout=1000 tqdm
RUN python3.10 -m pip install --default-timeout=1000 typing-extensions
RUN python3.10 -m pip install --default-timeout=1000 torch==2.1.2
RUN python3.10 -m pip install --default-timeout=1000 ctransformers
RUN python3.10 -m pip install --default-timeout=1000 accelerate
RUN python3.10 -m pip install --default-timeout=1000 optimum
RUN python3.10 -m pip install --default-timeout=1000 auto-gptq
RUN python3.10 -m pip install --default-timeout=1000 flask
RUN python3.10 -m pip install --default-timeout=1000 outlines
RUN python3.10 -m pip install fastapi
RUN python3.10 -m pip install uvicorn

# Set working directory
WORKDIR /app

RUN mkdir -p models

# Copy the necessary files from your host to the container
COPY src/ ./src/

# Command to run when the container starts
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
