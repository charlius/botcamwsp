import requests
import json
class WspRepository():
    def __init__(self) -> None:
        self.token_wsp = "EAAZA0LuBg7yMBAAiVl6Epr2oCVFp2A376UaLVdZC9aliqYzjrScL5l6sjZCaXNZAmNoeC9LIf5VpJR9yD1G9KF9fCb6M0zjRWIz7IIoNni20oTsoZBZAOCus903ZCkODNnKVujB9Akl3rlCkHRCGysqHwU6iFW42ZCHdde3eBWJ2gQR49b7hlmDug5gtz4GEK245f1O9Ir8QNwZDZD"

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

    def send_menu_principal_button(self, phone="56961720045"):
        url = f"https://graph.facebook.com/v15.0/104981199191453/messages"

        payload = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f"{phone}",
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "header": {
                        "type": "video",
                        "video": {
                            "link": "https://andrescallis.cl/videos/video.mp4"
                        }
                    },
                    "body": {
                        "text": "Que quieres hacer? 🤔❔❔"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "000",
                                    "title": "Alertar a Familia⚠❗"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "001",
                                    "title": "Foto camaras📷"
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

    def send_template_principal(self, phone):
        url = "https://graph.facebook.com/v17.0/104981199191453/messages"

        headers = {
            "Authorization": f"Bearer {self.token_wsp}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": phone,
            "type": "template",
           "template": {
                "name": "TEMPLATE_NAME",
                "language": {
                "code": "es_ARG"
                },
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def get_media_url(self, id_media):
        
        url = f"https://graph.facebook.com/v15.0/232201759676698?phone_number_id={id_media}"

        payload={}
        headers = {
        'Authorization': f'Bearer {self.token_wsp}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def get_download_media(self, url):


        payload={}
        headers = {
        'Authorization': f'Bearer {self.token_wsp}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response)
