from aiogram import types
from aiogram import Dispatcher
from create_bot import bot,dp

from keyboards import kb_client   #импорт клавиатуры клиента

from data_base import sqlite_db   #импорт модуля sqlite_db из пакета data_base,что бы потом запустить ф-ию считывания бд

from keyboards import inline      #импорт модуля inline из пакета keyboards,что бы потом отправить ссылки на 'ссылки'

# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup= kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему : \nhttps://t.me/cosmetic_menu_bot')

# @dp.message_handler(commands=['Меню'])
async def cosmetiks_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)

# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id,'Режим работы : Вт-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id,'Адрес : ул.Колбасная 15')


#хендлер,что бы вызвать клавиатуру cо ссылками
# @dp.message_handler(commands=['/ссылки'])
async def links_commands(message: types.Message):
    await message.answer('Ссылки:', reply_markup=inline.inlineKeyboard)




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(cosmetiks_menu_command, commands=['Меню'])
    dp.register_message_handler(links_commands, commands=['Ссылки'])