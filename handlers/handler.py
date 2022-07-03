import os
from aiogram import types
from loader import dp

from features.convert_to_audio import convert_to_audio


@dp.message_handler(content_types=['text'])
async def catch_text(message: types.Message):
    if message.chat.type == 'private':
        name_audio = message.text.split()[0]
        await convert_to_audio(name_audio, message.text)
        await message.bot.send_chat_action(message.from_user.id, "upload_voice")
        await message.bot.send_audio(message.from_user.id, open(f'temp_audios/{name_audio}.mp3', "rb"))
        os.remove(f'temp_audios/{name_audio}.mp3')