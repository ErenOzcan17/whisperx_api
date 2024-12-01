from flask import Flask, request, jsonify
import whisperx
import torch
import os

# Flask uygulaması başlatılıyor
app = Flask(__name__)

# WhisperX modelini yükleyin
device = "cuda" if torch.cuda.is_available() else "cpu"  # GPU varsa CUDA kullanılır, yoksa CPU'ya geçilir
model = whisperx.load_model("medium", device=device)

# Bellek temizleme
torch.cuda.empty_cache()

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Ses dosyasını alın
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']

    # Geçici bir dosyaya kaydedin
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)

    # Ses dosyasını transkribe edin (Batch boyutunu burada kontrol edebilirsiniz)
    try:
        # Eğer batch boyutunu kontrol etmek istiyorsanız, 'batch_size' parametresini modelin transcribe fonksiyonuna verebilirsiniz.
        result = model.transcribe(audio_path, batch_size=1)  # Batch boyutunu 1 yaparak belleği optimize ediyoruz
    except RuntimeError as e:
        if "CUDA out of memory" in str(e):
            torch.cuda.empty_cache()  # Belleği temizle
            return jsonify({'error': 'CUDA out of memory, try reducing batch size or using CPU'}), 500
        else:
            raise e

    # Geçici dosyayı silin
    os.remove(audio_path)

    # Sonuçları JSON olarak döndürün
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
