"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое
"""

import locale


def main():

    system_encoding = locale.getpreferredencoding()
    words = ['сетевое программирование', 'сокет', 'декоратор']

    with open('test_file.txt', 'w+', encoding=system_encoding) as test:
        for word in words:
            test.write(word + '\n')

    print(test)

    with open('test_file.txt', 'r', encoding=system_encoding) as test:
        for t in test:
            print(t)


if __name__ == '__main__':
    main()
