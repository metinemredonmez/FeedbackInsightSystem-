import openai

def transcribe_audio(file_path: str, api_key: str) -> str:
    openai.api_key = api_key
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']
