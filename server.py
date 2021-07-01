from socket import AF_INET, SOCK_STREAM, socket
from time import time
import pickle


def init_socket():
    s = socket(AF_INET, SOCK_STREAM)
    address = ('', 8989)
    s.bind(address)

    try:
        s.listen()
    except OSError as error:
        print(f'Инициализация не прошла ошибка: {error}')
    else:
        print(f'Сервер запустился.')
        return s


def get_request(data: bytes) -> dict:

    request = {}
    try:
        request = pickle.loads(data)
    except pickle.UnpicklingError:
        print('Не удается распаковать сообщение, полученное от клиента')
    except TypeError:
        print('Получил не байтоподобный объект для распаковки')
    return request


def prepare_response(code: int) -> dict:

    alerts = {
        200: 'OK',
        202: 'Accepted',
        400: 'Bad request',
    }
    alert = alerts.get(code)
    result = {'response': code, 'time': time(), 'alert': alert}
    return result if alert else None


def set_response(request: dict) -> bytes:

    actions = {
        'presence': 200,
        'stop': 202,
    }

    try:
        action = request.get('action')
    except Exception as error:
        print(error)
        return b''
    code = actions[action] if action else 400
    try:
        return pickle.dumps(prepare_response(code))
    except pickle.PicklingError:
        print('Не удается упаковать сообщение для отправки клиенту')
        return b''


def process(sock: socket) -> None:

    msg_max_size = 640

    while True:
        conn, _ = sock.accept()
        try:
            data = conn.recv(msg_max_size)
        except OSError as error:
            print(f'Ошибка: \n{error}')
        else:
            request = get_request(data)
            print(request)

            response = set_response(request)
            if response:
                conn.send(response)
                conn.close()

            if request['action'] == 'stop':
                print('Остановка сервера')
                break


def main() -> None:
    server = init_socket()
    process(server)


if __name__ == '__main__':
    main()
