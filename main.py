import logging
import sys

import yaml

from logger import log_error, log_init
from server import Server


def main():
    open('log', 'w').close()
    logging.basicConfig(filename="log", level=logging.INFO)

    try:
        with open('config.yml') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        log_error('Нет конфигурационного файла')
        return

    server = Server(config['dbconf'], config['uniconf'])
    server.start()


if __name__ == "__main__":
    main()


# TODO: переписать всё на расте
