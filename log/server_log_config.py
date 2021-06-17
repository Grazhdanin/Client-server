import logging
from logging.handlers import TimedRotatingFileHandler
from functools import wraps



log_format = logging.Formatter(
    '%(asctime)s %(levelname)s %(module)s %(message)s')

rotation_handler = TimedRotatingFileHandler('log/server.log', 'midnight', 10, encoding='utf-8')
rotation_handler.setFormatter(log_format)

serv_log = logging.getLogger('server')
serv_log.setLevel(logging.INFO)
serv_log.addHandler(rotation_handler)


def flogging(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        serv_log.info(f'Вызвана функция "{func.__name__}" аргументы:({args} {kwargs}')

    return wrapped

