# Модуль для работы с данными игроков


# импорты
from configparser import ConfigParser
from help import  *
from field import check_saves

SCORES = {}
PLAYER = tuple()
SAVES = {}

def read_ini():
    global SCORES, SAVES
    config = ConfigParser()
    if config.read('data.ini', encoding='utf-8'):
        SCORES = {name : [int(n) for n in score.split(',')] for name, score in config['Scores'].items()}
        SAVES = {tuple(name.split(';')): [['' if c == '-' else c for c in field[i:i+3]] for i in range(0,9,3)] for name, field in config['Saves'].items()}
        return True if config['General']['first'] == 'yes' else False
    else:
        raise FileExistsError

def save_ini():
    config = ConfigParser()
    config['Scores'] = {name: '.'.join(str(n) for n in score) for name, score in SCORES.items()}
    config['Saves'] = {name: '.'.join(name) for name, field in SAVES.items()}
    with open('data.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


def player_name(bot_mode='', *, change_order=False):
    global PLAYER
    # ввод имени первого игрока
    if len(PLAYER) == 0:
        PLAYER = (input(MESSAGES[1]).lower(), )
    elif len(PLAYER) == 1:
        # в этот параметр необходимо передать строку ai1 или ai2
        if bot_mode:
            # добавить бота с уровнем сложности
            PLAYER = (PLAYER[0], bot_mode)
        else:
            # ввести имя второго игрока человека
            PLAYER = (PLAYER[0], input(MESSAGES[2]).lower())
    # для выбора символа поменять местами элементы кортежа
    # первый играет крестиком и ходит первым
    if change_order:
        PLAYER = (PLAYER[1], PLAYER[0])



def game_mode():
    global PLAYER
    # выбор режима игры
    while True:
        gm = input(MESSAGES[3]).lower()
        if gm in ANSWERS[3]:
            break
    # если одиночная
    if gm in ANSWERS[3][:3]:
        # есть ли сохранения для одиночной игры
        if save := check_saves():
            # восстановление уровня сложности и очерёдности хода
            PLAYER = save
            return
        # запрашиваем уровень сложности
        while True:
            dl = input(MESSAGES[4]).lower()
            if dl in ANSWERS[4]:
                break
        # добавляем имя бота к Player
        if dl in ANSWERS[4][:3]:
            dl = 'ai1'
        else:
            dl = 'ai2'
        player_name(dl)
    # если парная
    else:
        player_name()
        if save :=check_saves(single=False):
            # восстановление уровня сложности и очерёдности хода из сохранённой партии
            PLAYER = save
            return True


    # выбор очерёдности хода

    if not (input(MESSAGES[5]).lower() in ANSWERS[5]):
        player_name(change_order=True)



