"""
. В декораторе @log реализовать фиксацию функции, из которой была вызвана декорированная. Если имеется такой код:
@log
def func_z():
 pass

def main():
 func_z()
...в логе должна быть отражена информация:
"<дата-время> Функция func_z() вызвана из функции main"
"""

import logging
from logging.handlers import TimedRotatingFileHandler
from functools import wraps
from inspect import stack


log_format = logging.Formatter(
    '%(asctime)s %(levelname)s %(module)s %(message)s')

rotation_handler = TimedRotatingFileHandler('log_function.log', 'midnight', 10, encoding='utf-8')
rotation_handler.setFormatter(log_format)

func_log = logging.getLogger('task_2')
func_log.setLevel(logging.INFO)
func_log.addHandler(rotation_handler)


def log(func):
    @wraps(func)
    def wrapped():
        s = stack()[1][3]  # (frame, filename, lineno, function, code_context, index)
        func_log.info(f' Функция "{func.__name__}" вызвана из функции "{s}"')

#        print(f' Функция "{func.__name__}" вызвана из функции "{s}" файл({stack()[0][1]}) строка-{stack()[1][2]}')

    return wrapped


@log
def func_z():
    print('HEllO')


def main():
    func_z()


def xz():
    func_z()


main()
xz()