# WhisperX API (Dockerized)

WhisperX modelini localinize kurmak yerine, Docker konteyneri olarak çalıştırabilirsiniz. Bu kurulum için sisteminizde yalnızca iki ön koşul gereklidir:

- **CUDA 12.4**  
  İndirme: https://developer.nvidia.com/cuda-12-4-0-download-archive
  
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
    docker build -t whisperx-flask-api .
    ```

3. Konteyneri çalıştırın:
    ```bash
    docker run --gpus all -d -p 5000:5000 whisperx-flask-api
    ```

## API'yi Test Etme

Konteyner çalıştıktan sonra, transkripsiyon uç noktasına bir `.wav` dosyası göndererek API'yi test edebilirsiniz:

```bash
curl -X POST -F "audio=@audio.wav" http://127.0.0.1:5000/transcribe
