import logging
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import pickle
import time

from homework.lesson_3.log.server_log_config import logger

s = socket(AF_INET, SOCK_STREAM)


def init_socket():
    s.bind(('', 8779))
    s.listen(5)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


def main():
    while True:
        client, addr = s.accept()
        logger.info('Получен запрос на соединение от %s' % str(addr))
        data = client.recv(1024)
        response = {
            'time': time.time(),
            'response': 200,
            'alert': 'Hello'
        }
        client.send(pickle.dumps(response))

        client.close()


if __name__ == '__main__':
    init_socket()
    try:
        main()
    except Exception as er:
        logger.error('The server did not start')


