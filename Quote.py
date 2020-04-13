import json
import requests

url = "https://api.quotable.io/random"


def getQuote():
    r = requests.get(url)
    conv_json = json.dumps(r.text)
    return r.json()

