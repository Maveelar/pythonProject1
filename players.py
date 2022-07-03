# Модуль для работы с данными игроков


# импорты
from configparser import ConfigParser
from scores import PLAYERS

PLAYERS = {}
PLAYER = tuple()
SAVES = {}

def read_ini():
    global PLAYERS, SAVES
    config = ConfigParser()
    if config.read('data.ini', encoding='utf-8'):
        PLAYERS = {name : [int(n) for n in score.split(',')] for name, score in config['Scores'].items()}
        SAVES = {tuple(name.split(';')): [['' if c == '-' else c for c in field[i:i+3]] for i in range(0,9,3)] for name, field in config['Saves'].items()}
        return True if config['General']['first'] == 'yes' else False
    else:
        raise FileExistsError

def save_ini():
    config = ConfigParser()
    config['Scores'] = {name: '.'.join(str(n) for n in score) for name, score in PLAYERS.items()}
    config['Saves'] = {name: '.'.join(name) for name, field in SAVES.items()}
    with open('data.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


def player_name(ai=''):
    global  PLAYER
    # если имя игрока ещё не вводилось
    if len(PLAYER) == 0:
        PLAYER = (input().lower())
    elif len(PLAYER) == 1:
        if not ai:
            PLAYER = (PLAYER[0], input().lower())
        else:
            # добавить имя бота с уровнем сложности
            PLAYER = (PLAYER[0], ai)
    else:
        # для выбора символа поменять местами элементы кортежа
        pass