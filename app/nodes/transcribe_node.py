import openai

class TranscribeNode:
    def __init__(self, api_key):
        openai.api_key = api_key

    def run(self, file_path: str):
        with open(file_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return {"transcribed_text": transcript['text']}
