class SendWsp():

    def __init__(self, wsp_repo):
        self.wsp_repo = wsp_repo

    def send_txt(self, txt):
        result = self.wsp_repo.sendtxt(txt)
        return result
    
    def send_image(self, name, phone):
        result = self.wsp_repo.send_image(name, phone)
        return result

    def send_video(self, name, phone):
        result = self.wsp_repo.send_video(name, phone)
        return result
