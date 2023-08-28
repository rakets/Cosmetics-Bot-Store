from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')

b4 = KeyboardButton('поделиться номером',request_contact=True)                  # спец.кнопка,получает номер
b5 = KeyboardButton('отправить где я',request_location=True)                    # спец.кнопка,получает локацию

kb_client = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)    # аргумент resize_keyboard=True делает,что кнопки изменяют размер под содержимое(сужаются)
                                                                                # аргумент one_time_keyboard удаляет клавиатуру,после выбора кнопки(можно вернуть клавиатуру)
# kb_client = ReplyKeyboardMarkup()                                             # без аргумента кнопки будут просто все одиноковые

kb_client.add(b1).add(b2).add(b3).row(b4, b5)                                   # добавление кнопок в клавиатуру

