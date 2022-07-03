# Модуль работы со справкой

from shutil import get_terminal_size as gts
from math import floor, ceil

h = '''Правила игры:


Список команд:


'''


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

