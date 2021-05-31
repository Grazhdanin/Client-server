"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""


def main():
    words = ('class', 'function', 'method')
    for word in words:
        word_bytes = bytes(word, 'utf-8', 'replace')
        print(f'word->{word}, type:{type(word)}|||len={len(word)}')


if __name__ == '__main__':
    main()
