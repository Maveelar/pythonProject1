# Модуль работы с полем игры

from players import PLAYER, SAVES
from help import MESSAGES, ANSWERS



FIELD = [['']*3 for _ in range(3)]


def field():
    global FIELD
    pass

# проверка наличия сохраненной партии для одиночной игры
def check_saves(*, single=True):
    global FIELD
    # для одиночной игры
    s = set(PLAYER)
    # для парной игры
    if not single:
        s |= {'ai1', 'ai2'}
    for save in SAVES:
        if set(save).issubset(s):
            load = input(MESSAGES[6]).lower()
            if load in ANSWERS[6]:
                FIELD = SAVES(save)
                return save
        return False