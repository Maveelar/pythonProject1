# Модуль верхнего уровня приложения крустики-нолики

# импорты
from help import *
from players import *


# приветствие
show_message('КРЕСТИКИ-НОЛИКИ')

# чтение .ini файла

if read_ini():
    show_help()


# запуск суперцикла

while True:

    command = input(' _> ')

    if command in ('quit', 'выход'):
        # обработка завершения работы приложения
        break
    if command in ('quit', 'выход'):
        break
    elif command in ('new', 'yes', 'новая', 'да'):
        # есть ли текущий игрок
        if not PLAYER:
            # начало новой партии
            player_name()
