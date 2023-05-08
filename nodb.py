import requests
import json


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")

    # parses json into python dict
    json_data = json.loads(response.text)

    # gets content at quote key and author key from dictionary
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote
