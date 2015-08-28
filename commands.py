import os
import random
import requests
import subprocess
from urllib import parse


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

def walrii(tg, message):
    tg.send_sticker(message.chat.id, "BQADBAADMwEAAlthFwM-reg8-6kV6QI")

def xkcd(tg, message):
    def _lastest_xkcd(tg, message):
        r = requests.get("http://xkcd.com/info.0.json").json()
        tg.send_message(message.chat.id, "'{} - {} - {}".format(r['title'], r["img"], r["alt"]))

    array = message.text.split(" ", 1)
    if len(array) < 2:
        _lastest_xkcd(tg, message)
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

def fortune(tg, message):
    # subprocess.check_output('fortune').decode('utf-8')
    allowed_fortunes = [ f for f in os.listdir("/usr/share/games/fortunes") if '.' not in f]
    array = message.text.split(" ", 1)
    if len(array) > 2:
        print(message.chat.id, "Too much arguments. EXTERMINATE!")
    elif len(array) == 1:
        tg.send_message(message.chat.id,
                        subprocess.check_output(['fortune',
                                                 random.choice(allowed_fortunes)]
                                               ).decode('utf-8')
                       )
    elif array[1] == '-l' or array[1] == '--list':
        result = "Here are the fortunes I have, pathetic human : \n"
        for file in allowed_fortunes:
            result += file+'\n'
        tg.send_message(message.chat.id, result)
    elif array[1] in allowed_fortunes:
        tg.send_message(message.chat.id, subprocess.check_output(['fortune', array[1]]).decode('utf-8'))
    else:
        tg.send_message(message.chat.id, "Invalid fortune. EXTERMINATE")

