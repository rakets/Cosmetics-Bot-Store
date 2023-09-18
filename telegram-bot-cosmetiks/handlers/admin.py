from aiogram.dispatcher import FSMContext  # для аннотации типа

from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import types

from aiogram import Dispatcher  # импорт диспетчера для аннотации типа

from create_bot import dp  #импорт экземпляра диспетчера

from aiogram.dispatcher.filters import Text

from create_bot import bot  #импорт экземпляра бота

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#Проверка является ли пользовательл админом
# dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_change_commands(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что нужно?') #reply_markup=button_case_admin)
    await message.delete()

# Начало диалога(загрузка нового пунката меню)
# dp.message_handler(commands=['Загрузить'],state=None)
async def dl_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        print('админ начал загрузку')
        await message.reply('Загрузи фото')

#Хендлер ОТМЕНЫ
# dp.message_handler(commands='отмена', state="*")
# dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()                             #получение состояние get_state бота
        if current_state is None:                                           #проверка состояния на None
            return None
        await state.finish()                                                #закрываем машину состояний,если бот не пустой
        print('админ отменил загрузку')
        await message.reply('Ok')                                           #вывод сообщения от бота

# Хендлер,который ловит первое сообщение(фото)
# dp.message_handler(content_types=['photo'],state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        print('фото загрузили')
        await FSMAdmin.next()  # хендлер переведен в состояние ожидания след.ответа
        print('бот перешел в новый хендлер')
        await message.reply('Теперь введи название')  # бот отправляет фразу,для получения ответа

# Хендлер,который ловит второе сообщение(название)
# dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        print('Пользователь ввел имя')
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')

# Хендлер,который ловит третье сообщение(описание)
# dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи цену')

# Хендлер,который ловит четвертое сообщение(цену)
# dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        async with state.proxy() as data:
            await message.reply(str(data))
        await state.finish()

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


