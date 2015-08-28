#!/usr/bin/python3
import configparser

from app.telegram import Telegram, Message
from app.handlers.logger_handler import LoggerHandler
from app.handlers.command_dispatcher import CommandDispatcher

import commands

def load_functions_from_module(cd, module):
    for f in [f for f in module.__dict__ if not f.startswith('_')]:
        cd.add_command('/{}'.format(f), getattr(module, f))

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    tg = Telegram(config["Telegram"]["apiURL"],config["Telegram"]["token"])
    loggerHandler = LoggerHandler("chat.log")
    cd = CommandDispatcher()
    load_functions_from_module(cd, commands)

    tg.add_handler(loggerHandler)
    tg.add_handler(cd)

    tg.process_updates()

