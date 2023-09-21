from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

b1 = KeyboardButton('/Удалить')
b2 = KeyboardButton('/Загрузить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)    #замена стандартной клавиатуры на созданную

button_case_admin.add(b1).add(b2)