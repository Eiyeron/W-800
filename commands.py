import requests
from urllib import parse

def walrii(tg, message):
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

def _lastest_xkcd(tg, message):
    r = requests.get("http://xkcd.com/info.0.json").json()
    tg.send_message(message.chat.id, "'{} - {} - {}".format(r['title'], r["img"], r["alt"]))


def xkcd(tg, message):
    array = message.text.split(" ", 1)
    if len(array) < 2:
        lastest_xkcd(tg, message)
        return

    argument = message.text.split(" ", 1)[1]
    if not argument:
        _lastest_xkcd(tg, message)
    else:
        try:
            number = int(argument)
            r = requests.get("http://xkcd.com/{}/info.0.json".format(number)).json()
            tg.send_message(message.chat.id, "{} - {} - {}".format(r['title'], r["img"], r["alt"]))
        except ValueError:
            tg.send_message(message.chat.id, "That wasn't a number. EXTERMINATE!")
