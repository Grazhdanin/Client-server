import time
from socket import AF_INET, SOCK_STREAM, socket
import pickle


def init_socket() -> socket:
    s = socket(AF_INET, SOCK_STREAM)
    address = ('localhost', 8989)
    try:
        s.connect(address)
    except ConnectionRefusedError:
        print('Соединенте с сервером не установлено')
    except OSError as error:
        print(f'Инициализация не прошла ошибка: {error}')
    else:
        print(f'Соединенте с сервером установлено.')
        return s


def read_messages(sock: socket) -> None:
    try:
        print('Приветики')
        data = sock.recv(1024)
        print("Получено: %s" % data.decode('utf-8'))
    except Exception as e:
        pass


def format_message(_message):
    presence_msg = {
        "action": "message",
        "time": time.time(),
        "type": "status",
        "user": 'user',
        "message": _message
    }

    return presence_msg


def write_to_server(sock: socket) -> None:
    while True:
        message = input('Введите сообщение: ')
        data = format_message(message)
        if data == 'exit':
            break
        # data = pickle.dumps(message)
        data = pickle.dumps(format_message(message))
        sock.send(data)


def main() -> None:
    conn = init_socket()
    if conn:
        mode = input('Выберите режим r/w: ')
        try:
            if mode == 'r':
                read_messages(conn)
            elif mode == 'w':
                write_to_server(conn)
        except Exception as error:
            print(f'Unexpected error: {error}')


if __name__ == '__main__':
    main()

