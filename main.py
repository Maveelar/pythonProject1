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

    command = input(MESSAGES[0])

    # выход из программы
    if command in COMMANDS('quit'):
        # обработка завершения работы приложения
        break
    # показать справку
    elif command in COMMANDS('help'):
        show_help()
    elif command in COMMANDS('scores'):
        pass
    # начало новой партии
    elif command in COMMANDS('new'):
        # есть ли текущий игрок
        if not PLAYER:
            # запрос имени игрока
            player_name()

        if game_mode():
            # продолжаем сохранённую партию
            pass
        else:
            # начинаем новую партию
            pass