import logging.handlers

logger = logging.getLogger('app.client_log_log')


formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - '%(message)s' ")


file_handler = logging.FileHandler("app.client_log.log", encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

path = 'app_client_log.log'
file_handler = logging.handlers.TimedRotatingFileHandler(path, when='D', interval=1, encoding='utf-8')
file_handler.setFormatter(formatter)
# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    #logger.error('Тестовый запуск логирования')