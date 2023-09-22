# from aiogram import Bot, types                     #импортируем класс Bot и types(спец.типы данных,что бы можно было писать аннотации типов в функциях)
# from aiogram.dispatcher import Dispatcher          #из aiogram.dispatcher импорт класса Dispatcher(бот сможет улавливать события)
# from aiogram.utils import executor

# import os
# from create_bot import dp                         #импорт экземпляра диспатчера

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton   #импорт кнопки и клавиатуры

#клавиатура
inlineKeyboard = InlineKeyboardMarkup(row_width=1)

#кнопки ссылки
inlineButton1 = InlineKeyboardButton(text='You', url='https://www.youtube.com/')
inlineButton2 = InlineKeyboardButton(text='Hack', url='https://hackyeah.pl/')

inlineKeyboard.add(inlineButton1).add(inlineButton2)
