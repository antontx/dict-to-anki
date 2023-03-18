import requests
import json

ANKI_URL = "http://localhost:8765"

def main():
    testDeck = {
        "a" : "A",
        "b" : "B",
        "c" : "C"
    }

    newDeck("test","Basic (and reversed card)",testDeck)


def newDeck(deck_name, card_type, cards):
    deck = {
        "action": "createDeck",
        "version": 6,
        "params": {
            "deck": deck_name
        }
    }
    response = requests.post(ANKI_URL, json.dumps(deck))
    print(response.text)


    for front, back in cards.items():
        note_data = {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": {
                    "deckName": deck_name,
                    "modelName": card_type,
                    "fields": {
                        "Front": front,
                        "Back": back
                    },
                    "options": {
                        "allowDuplicate": False
                    },
                    "tags": []
                }
            }
        }

        response = requests.post(ANKI_URL, json.dumps(note_data))
        print(response.text)



if __name__ == '__main__':
    main()

