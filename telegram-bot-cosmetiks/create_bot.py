from aiogram import Bot                     #импортируем класс Bot и types(спец.типы данных,что бы можно было писать аннотации типов в функциях).При разбивке по модулям types отсюда убралось.
from aiogram.dispatcher import Dispatcher   #из aiogram.dispatcher импорт класса Dispatcher(бот сможет улавливать события)

from aiogram.contrib.fsm_storage.memory import MemoryStorage  #импорт класс хранилища MemoryStorage.MemoryStorage-простое хранилище, которое сохраняет данные в оперативной памяти компьютера

import os                                   #импорт модуля os,что бы могли прочитать токен из переменной среды окружения

# from config_bot_cosmetiks import TOKEN
# bot = Bot(token=TOKEN)                    #инициализируем бота и читаем токен

storage = MemoryStorage()                   #создание объекта-хранилища MemoryStorage (хранение в оперативке компа)

bot = Bot(token=os.getenv('TOKEN'))         #инициализируем бота и читаем токен
dp = Dispatcher(bot, storage=storage)       #инициализируем dispatcher и передаем туда экземпляр нашего бота bot
                                            #в аргумент хранилища storage передаем объект-хранилище

