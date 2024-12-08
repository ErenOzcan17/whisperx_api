FROM nvidia/cuda:12.4.0-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    git \
    xz-utils \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz && \
    tar -xvf cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz && \
    rm cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz && \
    cp -r cudnn-linux-x86_64-8.9.7.29_cuda12-archive/include/* /usr/local/cuda/include && \
    cp -r cudnn-linux-x86_64-8.9.7.29_cuda12-archive/lib/* /usr/local/cuda/lib64 && \
    chmod a+r /usr/local/cuda/lib64/* && \
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda:/usr/local/cuda' >> ~/.bashrc

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-x86_64.sh && \
    bash Miniconda3-py39_23.3.1-0-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-py39_23.3.1-0-Linux-x86_64.sh && \
    /opt/conda/bin/conda init bash

ENV PATH=/opt/conda/bin:$PATH

RUN conda create --name whisperx python=3.10 && \
    echo "conda activate whisperx" >> ~/.bashrc

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
