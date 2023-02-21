import requests
import json
class WspRepository():
    def __init__(self) -> None:
        self.token_wsp = "EAAZA0LuBg7yMBAIi5ndPZCiLCJl53tdzo3LvquDxwPgd28OD6JLgQ9Y1ZCLRpZBTr3uCw3XUJUILYLbgfLSvYcqW8JbpZCvtfqilzhCWxsQb67CBZAKSoXtom3ytnPLuP53pSNbPvDnSccJLZBKooSfJBKBjzYVN9ZBjSQLxQwgZCAiHCjZCdQqNKnelFZA5WCyHGlqpriaiEXrBgZDZD"

    def sendtxt(self, phone="56961720045", txt="default"):
        url = f"https://graph.facebook.com/v15.0/104981199191453/messages"

        payload = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{phone}",
        "type": "text",
        "text": {
            "preview_url": False,
            "body": f"{txt}"
        }
        })
        headers = {
        'Authorization': f'Bearer {self.token_wsp}',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    def send_image(self, name = "", phone="56961720045"):
        url = f"https://graph.facebook.com/v15.0/104981199191453/messages"

        payload = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{phone}",
        "type": "image",
        "image": {
            "link": f"https://hogarcam.com/imagen/{name}"
        }
        })
        headers = {
        'Authorization': f'Bearer {self.token_wsp}',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    def send_video(self, name = "", phone="56961720045"):
        url = f"https://graph.facebook.com/v15.0/104981199191453/messages"

        payload = json.dumps({
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{phone}",
            "type": "video",
            "video": {
                "link": f"https://hogarcam.com/video/output.mp4",
                "caption": f"video {name}"
            }
        })
        
        headers = {
        'Authorization': f'Bearer {self.token_wsp}',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

result = WspRepository().send_video()

print(json.dumps(result))