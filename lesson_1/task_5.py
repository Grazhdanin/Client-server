"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import platform
import subprocess
import chardet


def run_ping(arguments: list):
    ping = subprocess.Popen(arguments, stdout=subprocess.PIPE)
    for pong in ping.stdout:
        pong_detect = chardet.detect(pong)
        print(pong.decode(encoding=pong_detect['encoding']), type(pong.decode(encoding=pong_detect['encoding'])))


run_ping(['ping', '-n' if platform.system() == 'Windows' else '-c', '3', 'yandex.com'])
run_ping(['ping', '-n' if platform.system() == 'Windows' else '-c', '3', 'youtube.com'])
