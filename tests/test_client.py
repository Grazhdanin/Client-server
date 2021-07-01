from homework import client


def main_client() -> None:
    test_start_server()
    test_main()


def test_start_server():
    start_server = client.init_socket()
    start_server('error_localhost', 'error_port')


def test_main():
    error_data = client.main()
    error_data.s.recv(msg={})


if __name__ == '__main__':
    try:
        main_client()
    except Exception as error_test:
        print(error_test)
