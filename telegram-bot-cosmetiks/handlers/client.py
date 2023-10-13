from aiogram import types
from aiogram import Dispatcher
from create_bot import bot,dp

from keyboards import kb_client   #импорт клавиатуры клиента

from data_base import sqlite_db   #импорт модуля sqlite_db из пакета data_base,что бы потом запустить ф-ию считывания бд

from keyboards import inline      #импорт модуля inline из пакета keyboards,что бы потом отправить ссылки на 'ссылки'

from aiogram.dispatcher.filters import Text  #импорт встроенного фильтра Text,что бы хендлер реагировал на 2 колбека

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


#хендлер,что бы вызвать клавиатуру cо ссылками(инлайн кнопками)
# @dp.message_handler(commands=['/ссылки'])
async def links_commands(message: types.Message):
    await message.answer('Ссылки:', reply_markup=inline.inlineKeyboard)

#хендлер,что бы уловить команду test и отправлять нам инлайн кнопку
# @dp.message_handler(commands=['test'])
async def www_call(message: types.Message):
    print('handler srabotal')
    await message.answer('knopka:', reply_markup=inline.callbackKeyboard)

#хендлер,что бы уловить команду www
# @dp.callback_query_handler(text='www')
async def text_call(callback: types.CallbackQuery):
    print('handler callback srabotal')
    # await callback.answer('knopka narzata')             #текст 'knopka narzata' отображается в виде всплывающего окошка
    await callback.message.answer('knopka narzata')     #текст 'knopka narzata' отправляется ботом в чат
    await callback.answer('knopka narzata', show_alert=True)

answ = dict()        #словарь для проверки и записи проголосовавших пользователей

#хендлер голосования
@dp.message_handler(commands=['golos'])
async def golos(message: types.Message):
    print('start golosowania')
    await message.answer('Golosowanie za....', reply_markup=inline.callGoll)

# @dp.callback_query_handler(text = 'like_1')
# async def golos_plus(callback: types.CallbackQuery):
#     await callback.answer('wy progolosowali za')
#
# @dp.callback_query_handler(text = 'like_-1')
# async def golos_minus(callback: types.CallbackQuery):
#     await callback.answer('wy progolosowali protiv')


#хендлер обрабатывающий два колбека
@dp.callback_query_handler(Text(startswith='like_'))
async def gol_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:         #проверка голосовал ли пользователь(есть ли id пользователя в словаре)
        answ[f'{callback.from_user.id}'] = res         #добавляем id проголосовавшего пользователя и голос в словарь
        await callback.answer('Wy progolosowali')
    else:
        await callback.answer('Wy urze progolosowali')



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(cosmetiks_menu_command, commands=['Меню'])
    dp.register_message_handler(links_commands, commands=['Ссылки'])
    dp.register_message_handler(www_call, commands=['test'])
    dp.register_callback_query_handler(text_call, text='www')
