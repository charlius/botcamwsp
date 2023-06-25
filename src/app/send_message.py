class SendWsp():

    def __init__(self, wsp_repo):
        self.wsp_repo = wsp_repo

    def send_txt(self, txt="", phone=""):
        result = self.wsp_repo.sendtxt(txt=txt, phone=phone)
        return result
    
    def send_image(self, name, phone):
        result = self.wsp_repo.send_image(name=name, phone=phone)
        print(" entro al enviar imagen clase")
        return result

    def send_video(self, name, phone):
        result = self.wsp_repo.send_video(name=name, phone=phone)
        return result
    
    def send_video_or_imagen_button(self, phone):
        result = self.wsp_repo.send_video_or_imagen_button(phone=phone)
        return result

    def send_menu_principal_button(self, phone):
        result = self.wsp_repo.send_menu_principal_button(phone=phone)
        return result
    
    def send_template_principal(self, phone):
        result = self.wsp_repo.send_template_principal(phone=phone)
        return result