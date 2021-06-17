import logging
from functools import wraps

log_format = logging.Formatter(
    '%(asctime)s %(levelname)s %(module)s %(message)s')

log_handler = logging.FileHandler('log/client.log', encoding='utf-8')
log_handler.setFormatter(log_format)

client_log = logging.getLogger('client')
client_log.setLevel(logging.INFO)
client_log.addHandler(log_handler)


def flogging(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        client_log.info(f'Вызвана функция "{func.__name__}" аргументы:({args} {kwargs}')

    return wrapped
