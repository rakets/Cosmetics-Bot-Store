from aiogram.utils import executor          #из aiogram.utils импортируем executor что бы запустить бота,что бы он вышел в онлайн
from aiogram import Bot                     #импортируем класс Bot и types(спец.типы данных,что бы можно было писать аннотации типов в функциях).При разбивке по модулям types отсюда убралось.
from aiogram.dispatcher import Dispatcher   #из aiogram.dispatcher импорт класса Dispatcher(бот сможет улавливать события)

# from config_bot_cosmetiks import TOKEN

import os                                   #импорт модуля os,что бы могли прочитать токен из переменной среды окружения

import json

import string

'''-------логинг ошибок------'''
import logging
logging.basicConfig(level=logging.INFO)
'''-------логинг ошибок------'''

bot = Bot(token=os.getenv('TOKEN'))           #инициализируем бота и читаем токен
# bot = Bot(token=TOKEN)                          #инициализируем бота и читаем токен

dp = Dispatcher(bot)                        #инициализируем dispatcher и передаем туда экземпляр нашего бота

async def on_startup(_):
    print('бот вышел в чат')

'''----тут у нас был декоратор,который улавливает любые сообщения----'''
# @dp.message_handler()                       #декоратор события,что в чат кто-то что-то пишет вообще
# async def echo_send(message : types.Message):
#     print('обработчик событий запущен')
#     await bot.send_message(message.from_user.id, message.text)
#
#     # if message.text == 'привет' or message.text == 'Привет':
#     #     print('ответное сообщение на "Привет" отправлено')
#     #     await message.answer('И тебе привет')      #отправка ответного сообщение нашим ботом.
#     # else:
#     #     await message.answer(message.text)
'''----------------------------------------------------------------------'''

'''-----------------------КЛИЕНТСКАЯ ЧАСТЬ--------------------------------'''

'''-----------------------КЛИЕНТСКАЯ-ЧАСТЬ--------------------------------'''

'''-----------------------ОБЩАЯ-ЧАСТЬ--------------------------------'''


'''-----------------------ОБЩАЯ-ЧАСТЬ--------------------------------'''


