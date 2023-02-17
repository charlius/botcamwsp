import requests
import json
class WspRepository():
    def __init__(self) -> None:
        self.token_wsp = "EAAZA0LuBg7yMBAFxXOzsxO9Swxp9UKKhbotYG64NapMnx9bkqclQkzcC4o11dqywvLJ4smeXBIxkTdxjDvWfRoZAj3VrD8MEyakzeinZAR1Nb6YK8bfEGZC9ONMqeWW959F8DDonX3PHN1dyePopFopKe4kGZAi6piyZBoGJDNS47ZBC9uIqNwwYBUb8EZBbg8BSheeVa8wKrAZDZD"

    def sendtxt(self, phone="56961720045"):
        url = f"https://graph.facebook.com/v15.0/104981199191453/messages"

        payload = json.dumps({
        "messaging_product": "whatsapp",
        "to": f"{phone}",
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
            "code": "en_US"
            }
        }
        })
        headers = {
        'Authorization': f'Bearer {self.token_wsp}',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
