import sqlite3 as sq

from create_bot import bot  #импортируем экземпляр бота

# функция подключения БД
def sql_start():
    global base, cur
    base = sq.connect('cosmetics_cool.db')  # подключение к базе данных или ее создание,если ее нет
    cur = base.cursor()                     # часть бд,осуществляет поиск,выборку и т.д
    if base:
        print('Data base connected!')       # если к базе нормально подключились выведет сообщ в консоль
        base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
        base.commit()

# функция,которой будем записывать изменения в бд,после добавления новой записи Меню (см файл 'База данных для бота sqlite')
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

#функция,которая срабатывает при нажатии на кнопку 'Меню' по sql-запросу выгружает все данные из таблицы в виде списка и помещаем это все
# в переменную ret.Далее через оператор await отправляем каждую строку таблицы пользователю в личку.(см файл 'База данных для бота sqlite')
async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

# функция что бы прочитать выборку из БД и извлечь  эти данные,что бы потом отправить админу с кнопкой 'Удалить'  (см файл 'База данных для бота sqlite')
async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()

# функция,которая посылает sql-запрос в БД удалить по названию data конкретную запись (см файл 'База данных для бота sqlite')
async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()
