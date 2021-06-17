from socket import socket, AF_INET, SOCK_STREAM
import pickle
import time

import logging
from log.client_log_config import flogging, client_log


s = socket(AF_INET, SOCK_STREAM)

@flogging
def init_socket():
    s.connect(('localhost', 8779))

@flogging
def main():
    msg = {
        "action": "authenticate",
        "time": time.time(),
        "user": {
            "account_name": "C0deMaver1ck",
            "password": "CorrectHorseBatteryStaple"
        }
    }
    s.send(pickle.dumps(msg))
    data = s.recv(1024)
    client_log.info(f"Сообщение от сервера:', {pickle.loads(data)}, 'длинной ', {len(data)}"),
    s.close()


if __name__ == '__main__':
    init_socket()
    main()
