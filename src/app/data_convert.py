import json

class DataConvert():

    def get_data(self, data):
        error = {}
        data = json.loads(data)
        entry = data.get("entry", [])
        if not entry:
            return error

        changes = entry[0].get("changes", [])
        if not changes:
            return error

        message = changes[0].get("value", {}).get("messages", [])
        if not message:
            return error

        if "text" in message[0].get("type", ""):
            phone = message[0].get("from", "none")
            text =  message[0].get("text", {}).get("body", "none")
            id = message[0].get("id", "")
            return {"phone": phone, "message": text, "id": id}

        if "interactive" in message[0].get("type", ""): 
            print(data)
            phone = message[0].get("from", "none")
            text = message[0].get("interactive", {}).get("button_reply", {}).get("id", "0")
            id = message[0].get("id", "")
            return {"phone": phone, "message": text, "id": id}
        print(data)
        return {}
