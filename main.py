#!/usr/bin/python3
import configparser

from app.telegram import Telegram, Message
from app.telegram_update_fetcher import TelegramUpdateFetcher
from app.handlers.logger_handler import LoggerHandler
from app.handlers.command_dispatcher import CommandDispatcher

def Walrii(tg, message):
    tg.send_sticker(message.chat.id, "BQADBAADMwEAAlthFwM-reg8-6kV6QI")

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    tg = Telegram(config["Telegram"]["apiURL"],config["Telegram"]["token"])
    loggerHandler = LoggerHandler("chat.log")
    cd = CommandDispatcher()
    cd.add_command("/walrii", Walrii)

    tg.add_handler(loggerHandler)
    tg.add_handler(cd)

    tfu = TelegramUpdateFetcher(tg)
    tfu.process_updates()
