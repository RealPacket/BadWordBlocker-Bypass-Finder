import random
from Words import words
import subprocess

try:
    import requests as req
except ImportError:
    print("Importing requests failed, running pip install requests")
    subprocess.run(["pip", "install", "requests"])
    import requests as req
import time as T

targetChannel: int = 763924031614746684  # I don't know.
used_words = set()
# My Test Server: https://discord.com/api/v9/channels/1066004152855056470/messages
# Their Test Server: https://discord.com/api/v9/channels/738533467364655164/messages
API: str = "https://discord.com/api/v9/channels/738533467364655164/messages"


def split_word(word):
    mid = len(word) // 2
    return f"{word[:mid]}<#{targetChannel}>{word[mid:]}"


random_word = random.choice(words)

headers = dict(Authorization=input("> Please enter a token!\n> "))
data = {
    "content": f"{split_word(random_word)}",
    "tts": False
}

while True:
    random_word = random.choice(words)
    data["content"] = split_word(random_word)
    if random_word in used_words:
        continue
    used_words.add(random_word)
    Response: req.Response = req.post(API, headers=headers, data=data)
    print(f"Testing {data['content']}")
    T.sleep(2)
