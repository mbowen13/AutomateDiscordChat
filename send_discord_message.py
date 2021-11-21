import requests
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
DISCORD_ENDPOINT = os.getenv('DISCORD_ENDPOINT')


def generateRandomNumber(max_seconds):
    SLOW_MODE_WAIT_TIME = 3
    return random.randint(SLOW_MODE_WAIT_TIME, max_seconds)


def sendChannelMessage(content_list):
    payload = {
        'content': random.choice(content_list)
    }

    header = {
        'authorization': AUTH_TOKEN

    }

    r = requests.post(DISCORD_ENDPOINT,
                      data=payload, headers=header)


def getChannelMessages():
    header = {
        'authorization': AUTH_TOKEN

    }

    r = requests.get(DISCORD_ENDPOINT,
                     headers=header)

    return [element['content'] for element in r.json()]


while True:
    messages = getChannelMessages()
    print(messages)
    for _ in messages:
        sendChannelMessage(messages)
        time.sleep(generateRandomNumber(20))
