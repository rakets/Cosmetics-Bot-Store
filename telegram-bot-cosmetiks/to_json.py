# импортируем модуль json
# создаем пустой список ar,
# открываем для чтения наш текстовый документ cenz_cosmetiks.txt в кодировке utf-8.Проходимся построчно циклом for(т.е читаем информацию из дока,переводим на всякий случай все
# в нижний регистр(с помощью lover),разбиваемс(с помощьюсsplit) по разделителю (перенос строки \n).Т.к там в строке
#  есть знак абзаца,то получаются списки из слова и служебного символа абзаца.Берем по индексу 0 это слово,проверяем
#  что бы там не была пустая строка и добавляем в список ar.

# открываем на запись(сам создастся) файл с расширением json (cenz_cosmetiks.json),открываем его для чтения ('w'),в кодировке
# utf-8.Используем из модуля json ф-ию .dump(позволяет записать данные в json файл),передаем туда первый аргумент(наш
# список из слов ar),второй агрумент(сам объект чтения e)

import json

ar = []

with open('cenz_cosmetiks.txt',encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('cenz_cosmetiks.json','w', encoding = 'utf-8') as e:
    json.dump(ar, e)