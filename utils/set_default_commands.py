from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await message.bot.send_message(message.chat.id, 'Привет! 👋\n\n'
                                                    'Я могу синтезировать аудио из текста.'
                                                    ' Для этого просто отправьте мне любой текст.')