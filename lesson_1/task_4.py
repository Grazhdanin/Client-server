"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""


def main():
    words = ('разработка', 'администрирование', 'protocol', 'standard')
    for word in words:
        my_encode = word.encode()
        print(my_encode)
        my_decode = my_encode.decode()
        print(my_decode)


if __name__ == '__main__':
    main()
