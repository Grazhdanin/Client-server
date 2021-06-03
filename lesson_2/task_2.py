"""
Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json
import locale


def write_order_to_json(item: str, quantity: int, price: int, buyer: str,
                        date: str):

    system_encoding = locale.getpreferredencoding()
    file_name = 'orders.json'
    file_json = {'orders': [
        {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
    ]}
    with open(file_name, 'w', encoding=system_encoding) as file:
        json.dump(file_json, file, indent=4)


def main():
    write_order_to_json('BRAUN BT3240', 30, 3670, 'Sergey Salomo', '03.06.2021')


if __name__ == '__main__':
    main()
