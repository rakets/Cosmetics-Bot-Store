REM что бы служебная информация bat файла не спамила в консоль
@echo off

REM нужно активировать вирт.окружение.Принудительно вызываем bat файл через call что бы получить расположие бат
call %~dp0telegram-bot-cosmetiks\venv\Scripts\activate

REM нужно перейти команд.строкой в папку с нашим проектом.Записываем cd
cd %~dp0telegram-bot-cosmetiks

REM будем получать в скрипте токен из бат-файла.Создаем переменную среды окружения
set TOKEN=6511163742:AAFRWyTNRyJ2nuHNWvNT8pzXWpWG3-4mnAo

REM запуск скрипта python(указываем файл,который нужно запустить)
python bot_telegram_cosmetiks.py

REM если в скрипте будет ошибка,то окно команд.строки закроется.поэтому пишем команду pause
pause

