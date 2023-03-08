import requests
import json
class WspRepository():
    def __init__(self) -> None:
        self.token_wsp = "EAAZA0LuBg7yMBABsq2dJYjvrG1B7OgTSiA39fh9GuHcGr0jkjutYsRaX6XTzED4SZANEncCZCI1G1XvHwgz3lpDsr8ZB98kGVd8ZCh2MHjYvnbHeQIWoNuQ8zMZCZAjoMDRRgNey7OGJUKNOFDKFvQ7MSd5BVH3yCYdxsCnRMSlidONeni7ZBA6ZAwavJNknnt6rsZCdPxpudLqwZDZD"

    def sendtxt(self, phone="56961720045", txt="default"):
        url = f"https://graph.facebook.com/v15.0/104981199191453/messages"
        print(phone)
        payload = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone,
        "type": "text",
        "text": {
            "preview_url": True,
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
            "link": f"https://hogarcam.com/duran/imagen/{name}"
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
        print("entro para enviar un video...")

        payload = json.dumps({
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{phone}",
            "type": "video",
            "video": {
                "link": f"https://rtsp.me/embed/f8RYNNr6/",
                "caption": f"video {name}"
            }
        })
        
        headers = {
        'Authorization': f'Bearer {self.token_wsp}',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    def send_video_or_imagen_button(self, phone="56961720045"):
        url = f"https://graph.facebook.com/v15.0/104981199191453/messages"

        payload = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f"{phone}",
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": "Que quieres ver? 🤔❔❔"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "001",
                                    "title": "📷imagen"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "002",
                                    "title": "🎥video"
                                }
                            }
                        ]
                    }
                }
            }
        )
        
        headers = {
        'Authorization': f'Bearer {self.token_wsp}',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()