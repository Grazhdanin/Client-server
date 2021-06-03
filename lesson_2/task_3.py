"""
Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь,
где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml


def write_data_to_yaml(data: dict, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)


def main():
    file = 'file.yaml'
    data = {
        'track': ['Sveta', 'Lena', 'Vika', 'A!...', 'Veronika!'],
        'integer': 113,
        'currency_signs': {
            'ruble_symbol': '\u20BD',
            'french_franc_sign': '\u20A3',
            'bitcoin_sign': '\u20BF'}
    }

    write_data_to_yaml(data, file)


if __name__ == '__main__':
    main()
