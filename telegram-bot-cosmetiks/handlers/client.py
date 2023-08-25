from aiogram import types
import string
import json

@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему : \nhttps://t.me/cosmetic_menu_bot')

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id,'Режим работы : Вт-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id,'Адрес : ул.Колбасная 15')
