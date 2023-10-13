# from aiogram import Bot, types                     #импортируем класс Bot и types(спец.типы данных,что бы можно было писать аннотации типов в функциях)
# from aiogram.dispatcher import Dispatcher          #из aiogram.dispatcher импорт класса Dispatcher(бот сможет улавливать события)
# from aiogram.utils import executor

# import os
# from create_bot import dp                         #импорт экземпляра диспатчера

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton   #импорт кнопки и клавиатуры

#------кнопоки-ссылки----------

#клавиатура для кнопок-ссылок
inlineKeyboard = InlineKeyboardMarkup(row_width=1)

#кнопки ссылки
inlineButton1 = InlineKeyboardButton(text='You', url='https://www.youtube.com/')
inlineButton2 = InlineKeyboardButton(text='Hack', url='https://hackyeah.pl/')

inlineKeyboard.add(inlineButton1).add(inlineButton2)

#-------колбек-кнопки-------------------------
callbackKeyboard =InlineKeyboardMarkup(row_width=1)

# callbackButton1 = InlineKeyboardButton(text='нажми кнопку', callback_data='www')
# callbackKeyboard.add(callbackButton1)

callbackKeyboard.add(InlineKeyboardButton(text='нажми кнопку', callback_data='www'))

#------------колбек-голосование------------------

callGoll = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                                 InlineKeyboardButton(text='No like', callback_data='like_-1'))
