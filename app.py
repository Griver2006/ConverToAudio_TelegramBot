from aiogram import executor

from loader import dp
import handlers
import utils.set_default_commands


if __name__ == '__main__':
    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
        except Exception:
            executor.start_polling(dp, skip_updates=True)