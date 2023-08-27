from aiogram.utils import executor          #из aiogram.utils импортируем executor что бы запустить бота,что бы он вышел в онлайн
from create_bot import dp

from handlers import client, admin, other   #импорт модулей,для запуска функций их хэндлеров

'''-------логинг ошибок------'''
import logging
logging.basicConfig(level=logging.INFO)
'''-------логинг ошибок------'''


async def on_startup(_):
    print('бот вышел в чат')

client.register_handlers_client(dp)         #запуск функии с хэндлерами модуля client
other.register_handlers_other(dp)           #запуск функии с хэндлерами модуля other

executor.start_polling(dp, skip_updates=True, on_startup = on_startup)      #команда запуска нажего бота

