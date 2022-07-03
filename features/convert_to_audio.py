import pyttsx3


async def convert_to_audio(name, text):
    engine = pyttsx3.init()
    engine.save_to_file(text, f'temp_audios/{name}.mp3')
    engine.runAndWait()