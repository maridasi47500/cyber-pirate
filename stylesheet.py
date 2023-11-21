from directory import Directory
from fichier import Fichier
class Css(Directory):
    def __init__(self,name):
        self.name=name
        self.content=Fichier("./css",name.split("/")[-1]).lire()
        self.css=True
    def get_html(self):
        return self.content.encode()
