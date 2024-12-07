import json
from flask import Flask, request, jsonify, Response
import whisperx
import torch
import os

# Flask uygulaması başlatılıyor
app = Flask(__name__)

if torch.cuda.is_available():
    model = whisperx.load_model("medium", device="cuda")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        audio_file = request.files['audio']
        # Sesi geçici bir dosyaya kaydediyorum
        audio_path = "temp_audio.wav"
        audio_file.save(audio_path)
    except KeyError:
        return Response(response="Audio file is missing in the request", status=400)
    except Exception:
        return Response(response="An error occurred while take the sound file", status=500)

    try:
        result = model.transcribe(audio_path, batch_size=16)
    except RuntimeError as e:
        return Response(response="An error occurred while processing the audio file", status=500)

    # Geçici dosyayı siliyorum
    os.remove(audio_path)
    return Response(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
