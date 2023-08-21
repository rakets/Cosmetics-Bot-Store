from aiogram.utils import executor          #из aiogram.utils импортируем executor что бы запустить бота,что бы он вышел в онлайн
from aiogram import Bot,types               #импортируем класс Bot и types(спец.типы данных,что бы можно было писать аннотации типов в функциях
from aiogram.dispatcher import Dispatcher   #из aiogram.dispatcher импорт класса Dispatcher(бот сможет улавливать события)

# from config_bot_cosmetiks import TOKEN

import os                                   #импорт модуля os,что бы могли прочитать токен из переменной среды окружения

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
@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему : \nhttps://t.me/cosmetic_menu_bot')

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вт-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул.Колбасная 15')

'''-----------------------КЛИЕНТСКАЯ-ЧАСТЬ--------------------------------'''

'''-----------------------ОБЩАЯ-ЧАСТЬ--------------------------------'''

@dp.message_handler()                      	 	#общий хендлер(декоратор событий,что в чат кто-то вообще пишет)
async def echo_send(message : types.Message):
    print('обработчик событий запущен(уловил сообщение)')
    await bot.send_message(message.from_user.id, message.text)

    if message.text == 'привет' or message.text == 'Привет':
         print('ответное сообщение на "Привет" отправлено')
         await message.answer('И тебе привет')
    else:
         await message.answer(message.text)

executor.start_polling(dp, skip_updates=True, on_startup = on_startup) #команда запуска нажего бота

'''-----------------------ОБЩАЯ-ЧАСТЬ--------------------------------'''


