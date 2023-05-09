import requests
import json


def get_inspo():
    response = requests.get("https://zenquotes.io/api/random")

    # parses json into python dict
    json_data = json.loads(response.text)

    # gets content at quote key and author key from dictionary
    inspo = json_data[0]['q'] + " - " + json_data[0]['a']
    return inspo
