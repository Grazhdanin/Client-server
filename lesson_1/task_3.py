"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""


def main():
    words = ('attribute', 'класс', 'функция', 'type')

    for word in words:
        try:
            bytes(word, 'ascii')
        except UnicodeEncodeError:
            print(f"Word '{word}' 'ascii' codec can't encode characters in position 0-4: ordinal not in range(128)")


if __name__ == '__main__':
    main()
