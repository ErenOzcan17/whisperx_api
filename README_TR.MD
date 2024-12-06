# WhisperX API (Dockerized)

WhisperX modelini localinize kurmak yerine, Docker konteyneri olarak çalıştırabilirsiniz. Bu kurulum için sisteminizde yalnızca üç ön koşul gereklidir:

- **CUDA 12.4**  
  İndirme: https://developer.nvidia.com/cuda-12-4-0-download-archive
  
- **CDUNN 8.9.7** \
  Kurulum komutları:
    ```bash
    wget https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz && \
    tar -xvf cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz && \
    cp -r cudnn-linux-x86_64-8.9.7.29_cuda12-archive/include/* /usr/local/cuda/include && \
    cp -r cudnn-linux-x86_64-8.9.7.29_cuda12-archive/lib/* /usr/local/cuda/lib64 && \
    chmod a+r /usr/local/cuda/lib64/* && \
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda:/usr/local/cuda' >> ~/.bashrc
    ```
  
- **NVIDIA Container Toolkit**  
  Kurulum Kılavuzu: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

Diğer tüm bağımlılıklar Docker konteynerine dahil edilmiştir.

## Projeyi Docker ile Çalıştırma Adımları

1. Depoyu klonlayın:
    ```bash
    git clone https://github.com/ErenOzcan17/whisperx_api.git
    cd whisperx_api
    ```

2. Docker imajını oluşturun:
    ```bash
    sudo docker build -t whisperx_api_image .
    ```

3. Konteyneri çalıştırın:
    ```bash
    sudo docker run -p 5000:5000 --gpus all --name whisperx_api whisperx_api_image
    ```

## API'yi Test Etme

Konteyner çalıştıktan sonra, transkripsiyon uç noktasına bir `.wav` dosyası göndererek API'yi test edebilirsiniz:

```bash
curl -X POST -F "audio=@audio.wav" http://127.0.0.1:5000/transcribe
