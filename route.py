from directory import Directory
from render_figure import RenderFigure
from user import User
import re

class Route():
    def __init__(self):
        self.Program=Directory("mon petit guide de python")
        self.Program.set_path("./")
        self.render_figure=RenderFigure(self.Program)
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def save_user(self,params={}):
        return self.render_figure.render_figure("welcome/datareach.html")
    def data_reach(self,search):
        return self.render_figure.render_figure("welcome/datareach.html")
    def run(self,redirect=False,redirect_path=False,path=False,params={}):
        if redirect:
            self.redirect=redirect
        if redirect_path:
            self.redirect_path=redirect
        if not self.render_figure.partie_de_mes_mots(balise="section",text=self.Program.get_title()):
            self.render_figure.ajouter_a_mes_mots(balise="section",text=self.Program.get_title())
        if path:
            ROUTES={'/': self.welcome,
                    '/save_user':self.save_user,
                    '/data_reach':self.data_reach,
                    }
            patterns=ROUTES.keys()
            functions=ROUTES.values()
            for pattern,case in zip(patterns,functions):
               print("pattern=",pattern)
               x=(re.match(pattern,path))
               print(x)
               if x:
                   return case(params)
