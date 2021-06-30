import time
from socket import socket, AF_INET, SOCK_STREAM
import pickle
from threading import Thread
import sys


def init_connection() -> socket:
    address = ('localhost', 8989)
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect(address)
    except ConnectionRefusedError:
        print('Соединенте с сервером не установлено')
    except OSError as error:
        print(f'Инициализация не прошла ошибка: {error}')
    else:
        print(f'Соединенте с сервером установлено.')
        return s


def write_request(conn: socket, action: str, **kwargs) -> None:
    request = None

    if action == 'presence':
        request = {
            'action': 'presence',
            'time': time.time(),
            'account_name': kwargs['account_name'],
        }

    if action == 'join':
        request = {
            'action': 'join',
            'time': time.time(),
            'room': kwargs['room'],
            'account_name': kwargs['account_name'],
        }

    if action == 'msg':
        request = {
            'action': 'msg',
            'time': time.time(),
            'to': kwargs['to'],
            'from': kwargs['frm'],
            'message': kwargs['msg'],
        }

    if request:
        try:
            conn.send(pickle.dumps(request))
        except OSError:
            pass


def parse(conn: socket, response: bytes) -> dict:
    try:
        response = pickle.loads(response)
    except EOFError:
        print('Сервер отключен')
        conn.close()
        sys.exit(0)
    print(response['alert'])
    if response['response'] != 200:
        conn.close()
        print('Закрыть')
        sys.exit(0)
    return response


def listen(conn: socket):
    while True:
        response = conn.recv(1024)

        try:
            response = pickle.loads(response)
        except EOFError:
            print('Сервер отключен')
            conn.close()
            sys.exit(0)

        if response.get('action') == 'msg':
            print(
                f'{response["from"]}: {response["message"]}')


def stream(sock: socket) -> None:
    account_name = input('Введите свое имя: ')
    write_request(sock, action='presence', account_name=account_name)
    parse(sock, sock.recv(1024))

    room = input('Выберите комнату ID: ')
    write_request(sock, action='join', room=room,
                  account_name=account_name)
    parse(sock, sock.recv(1024))

    listener = Thread(target=listen, args=(sock,))
    listener.daemon = True
    listener.start()
    print('Для ввыхода введите: q')

    while True:
        message = input()
        if message == 'q':
            sock.close()
            break
        write_request(sock, action='msg', to=room, frm=account_name,
                      msg=message)


def main():
    server = init_connection()
    stream(server)


if __name__ == '__main__':
    main()
