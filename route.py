from directory import Directory
from render_figure import RenderFigure
from user import User
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.Program=Directory("mon petit guide de python")
        self.Program.set_path("./")
        self.user=User()
        self.render_figure=RenderFigure(self.Program)
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def seeuser(self,params={}):
        getparams=("id",)
        myparam=dict(zip(getparams,params["routeparams"]))
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/showuser.html")
    def myusers(self,params={}):
        self.render_figure.set_param("users",User().getall())
        return self.render_figure.render_figure("welcome/users.html")
    def save_user(self,params={}):
        self.user=self.user.create(params)
        self.Program.set_redirect(red="/welcome")
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
                    "^/seeuser/([0-9]+)$":self.seeuser,
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
               if x:
                   params["routeparams"]=x.groups()

                   if not self.Program.get_redirect():
                     try:
                         self.Program.set_html(html=case(params))
                     except Exception:  
                         self.Program.set_html(html="<p>une erreur s'est produite "+str(traceback.format_exc())+"</p><a href=\"/\">retour à l'accueil</a>")
                   return self.Program
               else:
                   self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")

