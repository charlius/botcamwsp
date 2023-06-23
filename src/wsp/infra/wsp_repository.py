import requests
import json
class WspRepository():
    def __init__(self) -> None:
        self.token_wsp = "EAAZA0LuBg7yMBAEAejYW7Sgubx8ELo1ZCOZBMwXmNloWIEzGosnNWJSujtBrIDgAatSvoBkhP0c5o9Dk9UjGfRHIzdMyDnPNMTxKScaBKZAqkNhPRTFUM9Prvy5ZBAVujaGvargwtl3yhJoB9Lxs3PPjMZBCbgt9DZC5Cwa7QHgZBHG2UGQqD3SA3CNRkN2o9YhOlaH2OwQ6eAZDZD"

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
