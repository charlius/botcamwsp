class SendWsp():

    def __init__(self, wsp_repo) -> None:
        self.wsp_repo = wsp_repo

    def sendtxt(self):
        self.wsp_repo.sendtxt()
