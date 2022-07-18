# Модуль работы со справкой

from shutil import get_terminal_size as gts
from math import floor, ceil

SCORES = 'fake variable'

h = '''Правила игры:


Список команд:


'''

COMMANDS = {'quit': ('quit', 'выход'),
            'help': ('help', 'помощь', 'h', '?'),
            'scores': ('scores', 'таблица'),
            'new': ('new', 'yes', 'новая', 'да', 'y', 'n')}

MESSAGES = ('хотите начать новую партию? > ',
            'введите имя игрока > ',
            'введите имя второго игрока > ',
            'выберите режим игры:\n 1 - с ботом\n 2 - с игроком\n>',
            'выберите ровень сложности:\n 1 - легкий\n 2 - трудный\n>',
            'вы хотите ходить первым? >',
            'вы хотите загрузить сохранённую партию? >')

ANSWERS = (None,
           None,
           None,
           ('1', 'бот', 'б', '2', 'человек', 'ч'),
           ('1', 'лёгкий', 'л', '2', 'трудный', 'т'),
           ('yes', 'да', 'y', 'д')
           )

def show_help():
    print(h)


def show_message(text):
    widht = gts()[0] - 1
    half_widht = (widht - len(text) - 2) / 2
    m = f'''{'#' * widht}
{'#' + ' '*(widht-2) + '#'}
{'#' + ' '*ceil(half_widht) + text.upper() + ' '*floor(half_widht) + '#'}
{'#' + ' '*(widht-2) + '#'}
{'#'*widht}'''
    print(m, end='\n\n')

