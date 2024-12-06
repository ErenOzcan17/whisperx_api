#Docker Readme


Docker build almak için:
```bash
    sudo docker build -t whisperx_api_image .
   ```

Container kaldırmak için:
```bash
    sudo docker run -p 5000:5000 --gpus all --name whisperx_api whisperx_api_image
   ```

Container a istek atmak için
```bash
    curl -X POST -F "audio=@audio.wav" http://127.0.0.1:5000/transcribe
   ```