
#!/usr/bin/env python
import os
import sys
import logging
import logging.config
from slackbot import settings
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import datetime
from datetime import timedelta
import random

@respond_to('Say something', re.IGNORECASE)
def saysomething(message):
    quotes = [
        "Mos Eisley spaceport. You will never find a more wretched hive of scum and villainy.",
        "These aren't the droids you're looking for.",
        "I felt a great disturbance in the Force, as if millions of voices suddenly cried out in terror and were suddenly silenced.",
        "Only a Sith Lord deals in absolutes.",
        "I have a bad feeling about this.",
        "That's no moon. It's a space station",
        "You can't win, Darth. If you strike me down, I shall become more powerful than you could possibly imagine.",
        "Use the Force, Luke.",
        "So uncivilized.",
        "If you strike me down, I shall become more powerful than you can possibly imagine.",
        "I have the high ground.",
        "Hello there!",
        "You were the Chosen One!",
        "Who is more foolish? The fool or the fool who follows him?",
        "Remember… the Force will be with you. Always.",
        "I have failed you, Anakin. I have failed you.",
        "Be mindful of your thoughts, Anakin, they betray you."
    ]
    message.reply(random.choice(quotes))

@respond_to('Remember Alderaan?', re.IGNORECASE)
def remember(message):
    message.reply('Too soon dude, too soon...');

@respond_to('Who shot first?', re.IGNORECASE)
def shotfirst(message):
    message.reply('Han shot first.');

@listen_to('Star Wars', re.IGNORECASE)
def usetheforce(message):
    today = datetime.date.today()
    release = datetime.date(2019, 12, 20)
    days = release - today
    delta = timedelta()
    message.reply(
        ':thumbsup: Only {0} days until *Star Wars: Episode IX!'.format(days.days))


@respond_to('I love you', re.IGNORECASE)
def love(message):
    message.reply('I know.')


def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger(
        'requests.packages.urllib3.connectionpool').setLevel(logging.DEBUG)

    Bot().run()

if __name__ == "__main__":
    main()
