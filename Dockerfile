FROM nvidia/cuda:12.4.0-cudnn8-runtime-ubuntu22.04

# Gerekli bağımlılıkları yükle
RUN apt-get update

# Conda'yı kur
RUN apt-get install -y wget bzip2 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-x86_64.sh && \
    bash Miniconda3-py39_23.3.1-0-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-py39_23.3.1-0-Linux-x86_64.sh && \
    /opt/conda/bin/conda init bash

# Conda'yı PATH'e ekle
ENV PATH /opt/conda/bin:$PATH

# Conda ortamını oluştur ve aktif et
RUN conda create --name whisperx python=3.10 && \
    echo "conda activate whisperx" >> ~/.bashrc

# Proje kodlarını kopyalayın
COPY . /app

# Gereksinimlerinizi yükleyin
RUN pip install --no-cache-dir -r /app/requirements.txt


WORKDIR /app

# Flask API'yi çalıştırın
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
