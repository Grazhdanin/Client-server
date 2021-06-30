import time
from socket import socket, AF_INET, SOCK_STREAM
import pickle
import select


def init_connection() -> socket:
    address = ('', 8989)
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.settimeout(1)
    try:
        s.listen()
    except OSError as error:
        print(f'Инициализация не прошла ошибка: {error}')
    else:
        print(f'Сервер запустился.')
        return s


def set_response(request: dict) -> bytes:
    resp = {
        'response': 400,
        'time': time.time(),
        'alert': 'Bad request'
    }
    if request.get('action') == 'presence':
        resp = {
            'response': 200,
            'time': time.time(),
            'alert': f'{request["account_name"]} welcome on server!'
        }
    if request.get('action') == 'join':
        resp = {
            'response': 200,
            'time': time.time(),
            'alert': f'{request["account_name"]} joined room {request["room"]}'
        }
    if request.get('action') == 'msg':
        resp = {
            'response': 200,
            'action': 'msg',
            'time': time.time(),
            'from': f'{request["from"]}',
            'to': 'all',
            'message': request.get('message')
        }
    print('Responded %d', resp['response'])
    return pickle.dumps(resp)


def read_requests(r: list, clients: list) -> list:
    responses = []
    for talker in r:
        try:
            data = talker.recv(1024)
            print('Received data, length %d', len(data))
            request = pickle.loads(data)
            response = set_response(request)
            responses.append(response)
        except EOFError as e:
            clients.remove(talker)
            print('Connection with %s is closed', talker)
    return responses


def write_responses(responses: list, w: list, clients: list) -> None:
    for response in responses:
        for lists in w:
            try:
                lists.send(response)
            except ConnectionError as e:
                lists.close()
                clients.remove(lists)
                print('Connection with %s is closed', lists)


def mainloop(sock: socket) -> None:
    clients = []
    while True:
        try:
            client, addr = sock.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение с %s" % str(addr))
            clients.append(client)
        finally:
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], 10)
            except:
                pass
            responses = read_requests(r, clients)
            if responses:
                write_responses(responses, w, clients)


def main():
    server = init_connection()
    mainloop(server)


if __name__ == '__main__':
    main()
