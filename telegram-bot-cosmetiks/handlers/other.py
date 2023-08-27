from aiogram import types
import string
import json
from aiogram import Dispatcher
from create_bot import dp

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


# @dp.message_handler()                      	 	                        #общий хендлер(декоратор событий,что в чат кто-то вообще пишет)
# async def echo_send(message : types.Message):
#     print('обработчик событий запущен(уловил сообщение)')
#
#     # await bot.send_message(message.from_user.id, message.text)          #бот высылает пользователю тоже самое сообщение
#
#     if message.text == 'привет' or message.text == 'Привет':
#          print('ответное сообщение на "Привет" отправлено')
#          await message.answer('И тебе привет')
#
#     # else:
#     #      await message.answer(message.text)

# @dp.message_handler()
async def echo_send_mat(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open("cenz_cosmetiks.json")))) != set():
        # await message.reply('maty zapreszeny')
        user = message.from_user                                            #получение объекта user,что бы после получить из него имя пользователя
        await message.answer(f'@{user.first_name}!Маты запрещены!')          #достаем имя пользователя через user.first_name
        await message.delete()

def register_handlers_other(dp:Dispatcher):
    dp.register_message_handler(echo_send_mat)
