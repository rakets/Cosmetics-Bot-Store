from aiogram.dispatcher import FSMContext  # для аннотации типа

from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import types

from aiogram import Dispatcher  # импорт диспетчера для аннотации типа

from create_bot import dp  #импорт экземпляра диспетчера

from aiogram.dispatcher.filters import Text

from create_bot import bot  #импорт экземпляра бота

from data_base import sqlite_db     #импорт модуля sqlite_db из пакета data_base

from keyboards import admin_kb      #импорт модуля admin_kb из которого будем доставать клавиатуру для админа

from handlers import client

from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton   #необходимые компоненты,для создания кнопки удаления записи меню

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#Проверка является ли пользовательл админом
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_change_commands(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что нужно?', reply_markup=admin_kb.button_case_admin)
    await message.delete()

# Начало диалога(загрузка нового пунката меню)
# @dp.message_handler(commands=['Загрузить'],state=None)
async def dl_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        print('админ начал загрузку')
        await message.reply('Загрузи фото')

#Хендлер ОТМЕНЫ
# @dp.message_handler(commands='отмена', state="*")
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()                             #получение состояние get_state бота
        if current_state is None:                                           #проверка состояния на None
            return None
        await state.finish()                                                #закрываем машину состояний,если бот не пустой
        print('админ отменил загрузку')
        await message.reply('Ok')                                           #вывод сообщения от бота

#хендлер удаления записи из БД
# @dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))

# хендлеры удаления записи из БД и меню  (см файл 'База данных для бота sqlite')
# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def call_delete(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text = f'{callback_query.data.replace("del ", "")} удалены', show_alert=True)

# Хендлер,который ловит первое сообщение(фото)
# @dp.message_handler(content_types=['photo'],state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        print('фото загрузили')
        await FSMAdmin.next()  # хендлер переведен в состояние ожидания след.ответа
        print('бот перешел в новый хендлер')
        await message.reply('Теперь введи название')  # бот отправляет фразу,для получения ответа

# Хендлер,который ловит второе сообщение(название)
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        print('Пользователь ввел имя')
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')

# Хендлер,который ловит третье сообщение(описание)
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи цену')

# Хендлер,который ловит четвертое сообщение(цену)
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sqlite_db.sql_add_command(state)     #запуск ф-ии sql_add_command из модуля sqlite_db

        await state.finish()


# ------- это я добавил вывод в консоль количества проголосовавших пользователей,когда админ введет /ile   ------------
@dp.message_handler(commands=['ile'])                          #хендлер будет реагировать на ile
async def ile_golos(message: types.Message):
    print(f'progolosovalo {len(client.answ)} polzovateley')    #достаем длину словаря answ,созданного при голосвании в файле client
# -----------------------------------------------------------------------------------------------------


# Регистрация хендлеров
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(dl_start, commands=['Загрузить'], state=None)

    # 2 хендлера отмены
    dp.register_message_handler(cancel_handler, commands='отмена', state="*")
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")

    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)

    #Проверка является ли пользователь админом
    dp.register_message_handler(make_change_commands, commands=['moderator'], is_chat_admin=True)       #срабатывает,если пользователь является админом

    #хендлеры удаления записи из бд после нажатия кнопки
    dp.register_message_handler(delete_item, commands=['Удалить'])
    dp.register_callback_query_handler(call_delete, lambda x: x.data and x.data.startswith('del '))