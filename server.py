from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import pickle
import time

s = socket(AF_INET, SOCK_STREAM)


def init_socket():
    s.bind(('', 8777))
    s.listen(5)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


def main():
    while True:
        client, addr = s.accept()
        print('Получен запрос на соединение от %s' % str(addr))
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
        print('The server did not start')
