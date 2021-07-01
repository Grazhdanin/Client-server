
from socket import AF_INET, SOCK_STREAM, socket
from time import time
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


def set_request(action: str, user: str, status: str = None) -> bytes:

    requests = {
        'presence': {
            'action': action,
            'time': time(),
            'type': 'status',
            'user': {
                'account_name': user,
                'status': status
            }
        },
        'stop': {
            'action': action
        }
    }

    request = requests.get(action)
    try:
        return pickle.dumps(request) if request else None
    except pickle.PicklingError:
        print('Не удается упаковать сообщение для отправки на сервер')
        return b''


def get_response(data: bytes) -> dict:

    response = {}
    try:
        response = pickle.loads(data)
    except pickle.UnpicklingError:
        print('Не удается распаковать сообщение, полученное с сервера')
    except TypeError:
        print('Получил не байтоподобный объект для распаковки')
    return response


def main():
    msg_max_size = 100
    actions = ('presence', 'stop')
    user = 'XXX'
    status = 'online'

    for action in actions:
        request = set_request(action, user, status)
        conn = init_socket()
        if conn and request:
            conn.send(request)
            try:
                data = conn.recv(msg_max_size)
            except ConnectionError:
                print('Ошибка подключения')
            else:
                response = get_response(data)
                print(response)


if __name__ == '__main__':
    main()