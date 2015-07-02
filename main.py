#!/usr/bin/python3
import configparser
import requests
from urllib import parse

from app.telegram import Telegram, Message
from app.telegram_update_fetcher import TelegramUpdateFetcher
from app.handlers.logger_handler import LoggerHandler
from app.handlers.command_dispatcher import CommandDispatcher

def Walrii(tg, message):
    tg.send_sticker(message.chat.id, "BQADBAADMwEAAlthFwM-reg8-6kV6QI")

def ddg(tg, message):
    array = message.text.split(" ", 1)
    if len(array) < 2:
        tg.send_message(message.chat.id, "No argument given. EXTERMINATE!")
        return
    argument = message.text.split(" ", 1)[1]
    if not argument:
        tg.send_message(message.chat.id, "No argument given. EXTERMINATE!")
    else:
        tg.send_message(message.chat.id, "https://duckduckgo.com/?q="+parse.quote_plus(argument))

def lastest_xkcd(tg, message):
    r = requests.get("http://xkcd.com/info.0.json").json()
    tg.send_message(message.chat.id, "'{} - {} - {}".format(r['title'], r["img"], r["alt"]))


def xkcd(tg, message):
    array = message.text.split(" ", 1)
    if len(array) < 2:
        lastest_xkcd(tg, message)
        return

    argument = message.text.split(" ", 1)[1]
    if not argument:
        lastest_xkcd(tg, message)
    else:
        try:
            number = int(argument)
            r = requests.get("http://xkcd.com/{}/info.0.json".format(number)).json()
            tg.send_message(message.chat.id, "{} - {} - {}".format(r['title'], r["img"], r["alt"]))
        except ValueError:
            tg.send_message(message.chat.id, "That wasn't a number. EXTERMINATE!")


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    tg = Telegram(config["Telegram"]["apiURL"],config["Telegram"]["token"])
    loggerHandler = LoggerHandler("chat.log")
    cd = CommandDispatcher()
    cd.add_command("/walrii", Walrii)
    cd.add_command("/ddg", ddg)
    cd.add_command("/xkcd", xkcd)

    tg.add_handler(loggerHandler)
    tg.add_handler(cd)

    tfu = TelegramUpdateFetcher(tg)
    tfu.process_updates()
