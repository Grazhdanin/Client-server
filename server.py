import select
from socket import AF_INET, SOCK_STREAM, socket
import pickle


def init_socket():
    s = socket(AF_INET, SOCK_STREAM)
    address = ('', 8989)
    s.bind(address)
    s.settimeout(1)

    try:
        s.listen()
    except OSError as error:
        print(f'Инициализация не прошла ошибка: {error}')
    else:
        print(f'Сервер запустился.')
        return s


def mainloop(sock: socket) -> None:
    clients = []
    messages = []

    while True:
        try:
            conn, addr = sock.accept()
        except OSError:
            pass
        else:
            print("Получен запрос на соединение с %s" % str(addr))
            clients.append(conn)
        finally:
            r = []
            w = []
            print(clients)
            try:
                r, w, e = select.select(clients, clients, [], 10)
            except:
                pass

            for connected_client in r:
                print("хх %s" % str(addr))
                for item in messages:
                    try:
                        connected_client.send(pickle.loads(item))
                        messages.remove(item)
                    except Exception as e:
                        clients.remove(connected_client)

            for connected_client in w:
                print("ХХ %s" % str(addr))
                data = connected_client.recv(1024)
                message = pickle.loads(data)
                print(f' Пользователь -{addr} : {message}')
                # messages.append(message)
                messages.append(message['message'])


def main():
    server = init_socket()
    mainloop(server)


if __name__ == '__main__':
    main()
