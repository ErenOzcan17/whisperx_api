# WhisperX API(Dockerized)

Instead of installing the WhisperX model locally, you can run it as a Docker container. This setup requires only tree prerequisites on your system:

- **CUDA 12.4**  
  Download: https://developer.nvidia.com/cuda-12-4-0-download-archive

- **CDUNN 8.9.7** \
Installation Guide:
    ```bash
    wget https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz && \
    tar -xvf cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz && \
    cp -r cudnn-linux-x86_64-8.9.7.29_cuda12-archive/include/* /usr/local/cuda/include && \
    cp -r cudnn-linux-x86_64-8.9.7.29_cuda12-archive/lib/* /usr/local/cuda/lib64 && \
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda:/usr/local/cuda' >> ~/.bashrc
    ```
  
- **NVIDIA Container Toolkit**  
  Installation Guide: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

All other dependencies are included in the Docker container.

## Steps to Run the Project in Docker

1. Clone the repository:
    ```bash
    git clone https://github.com/ErenOzcan17/whisperx_api.git
    cd whisperx_api
    ```

2. Build the Docker image:
    ```bash
    docker build -t whisperx-flask-api .
    ```

3. Run the container:
    ```bash
    docker run --gpus all -d -p 5000:5000 whisperx-flask-api
    ```

## Testing the API

Once the container is up and running, you can test it by sending a `.wav` file to the transcription endpoint:

```bash
curl -X POST -F "audio=@audio.wav" http://127.0.0.1:5000/transcribe
