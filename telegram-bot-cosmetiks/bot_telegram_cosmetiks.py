from aiogram.utils import executor          #из aiogram.utils импортируем executor что бы запустить бота,что бы он вышел в онлайн

from create_bot import dp

from handlers import client, other, admin   #импорт модулей,для запуска функций их хэндлеров

from data_base import sqlite_db             #импорт модуля sqlite_db из пакета data_base

from keyboards import inline                #импорт модуля inline из пакета keyboards

'''-------логинг ошибок------'''
import logging
logging.basicConfig(level=logging.INFO)
'''-------логинг ошибок------'''


async def on_startup(_):
    print('бот вышел в чат')
    sqlite_db.sql_start()                   #запуск ф-ии записи бд

client.register_handlers_client(dp)         #запуск функции с хэндлерами модуля client
admin.register_handlers_admin(dp)           #запуск функции с хэндлерами модуля admin
other.register_handlers_other(dp)           #запуск функции с хэндлерами модуля other

executor.start_polling(dp, skip_updates=True, on_startup = on_startup)      #команда запуска нажего бота

