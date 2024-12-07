from flask import Flask, request, Response
import torch
import whisperx
import gc
import json
import os

app = Flask(__name__)
device = "cuda"
model = whisperx.load_model("medium", device, compute_type="float16")

@app.route('/', methods=['POST'])
def transcribe_and_diarize():
    try:
        audio_file = request.files['audio']
        audio_path = "temp_audio.wav"
        audio_file.save(audio_path)
    except KeyError:
        return Response(response="Audio file is missing in the request", status=400)
    except Exception as e:
        return Response(response=f"An error occurred: {str(e)}", status=500)

    try:
        # transcription
        audio = whisperx.load_audio(audio_path)
        result = model.transcribe(audio, batch_size=16)

        # purge memory
        gc.collect()
        torch.cuda.empty_cache()

        # align result
        model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

        # purge memory
        del model_a
        gc.collect()
        torch.cuda.empty_cache()

        # diarization
        diarize_model = whisperx.DiarizationPipeline(use_auth_token="<hf_token>", device=device)
        diarize_segments = diarize_model(audio)
        result = whisperx.assign_word_speakers(diarize_segments, result)

    except RuntimeError as e:
        return Response(response=f"An error occurred during processing: {str(e)}", status=500)
    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)

    return Response(json.dumps(result, ensure_ascii=False), content_type="application/json")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
