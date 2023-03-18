import json
import requests

API_KEY = open("tokens.txt","r").readline()

def fileToDict(path):
    file = open(path,"r")
    lines = file.readlines()

    dicts = {}
    current_dict = ""

    for line in lines:
        if line[0] == "#":
            current_dict = line[2:-1]
            dicts[current_dict] = {}
        elif line[0] == "*":
            dicts[current_dict][line[2:-1]] = "?"

    print(json.dumps(dicts, indent=4))

def translate(text):
    url = "https://api.deepl.com/v2/translate"

    params = {
        "auth_key": API_KEY,
        "text": text,
        "source_lang": "EN",
        "target_lang": "DE"
    }

    try:
        response = requests.post(url, data=params)
        response.raise_for_status()
        translation = json.loads(response.text)["translations"][0]["text"]
        return translation
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Request Exception:", err)

print(API_KEY)
path = "vocab.txt"
fileToDict(path)
print(translate("tree"))