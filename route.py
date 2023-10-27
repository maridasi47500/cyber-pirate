from directory import Directory
from render_figure import RenderFigure
from user import User
import re

class Route():
    def __init__(self):
        self.Program=Directory("mon petit guide de python")
        self.Program.set_path("./")
        self.user=User()
        self.render_figure=RenderFigure(self.Program)
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def myusers(self,params={}):
        self.render_figure.set_param("users",User().getall())
        return self.render_figure.render_figure("welcome/users.html")
    def save_user(self,params={}):
        self.user=self.user.create(params)
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
            ROUTES={

                    '/save_user':self.save_user,
                    '/data_reach':self.data_reach,
                    '/welcome':self.myusers,
                    '/': self.welcome,
                    }
            REDIRECT={"/save_user": "/welcome"}
            patterns=ROUTES.keys()
            functions=ROUTES.values()
            for pattern,case in zip(patterns,functions):
               print("pattern=",pattern)
               x=(re.match(pattern,path))
               print(x)
               if x:
                   try:
                       red=REDIRECT[x]
                       self.Program.set_redirect(redirect=red)

                   except:  
                       self.Program.set_html(html=case(params))
                   return self.Program

