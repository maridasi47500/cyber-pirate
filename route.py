from directory import Directory
from render_figure import RenderFigure
from centrale import Centrale
from machinealaver import Machinealaver

from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.Program=Directory("Ma laverie")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.dbCentrale=Centrale()
        self.dbMachinealaver=Machinealaver()
        self.render_figure=RenderFigure(self.Program)
        self.getparams=("id",)
    def set_my_session(self,x):
        print("set session",x)
        self.Program.set_my_session(x)
        self.render_figure.set_session(self.Program.get_session())
    def set_redirect(self,x):
        self.Program.set_redirect(x)
        self.render_figure.set_redirect(self.Program.get_redirect())
    def set_json(self,x):
        self.Program.set_json(x)
        self.render_figure.set_json(self.Program.get_json())
    def set_notice(self,x):
        print("set session",x)
        self.Program.set_session_params({"notice":x})
        self.render_figure.set_session(self.Program.get_session())
    def set_session(self,x):
          print("set session",x)
          self.Program.set_session(x)
          self.render_figure.set_session(self.Program.get_session())
    def get_this_route_param(self,x,params):
          print("set session",x)
          return dict(zip(x,params["routeparams"]))
          
    def logout(self,search):
        self.Program.logout()
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def machinealaver(self,search):
        print("hey")
        centrale=self.dbCentrale.getbyid(myid)
        print("centrale")
        machinealaver=self.dbMachinealaver.getallbycentraleid(myid)
        print("machinealaver")
        self.render_figure.set_param("centrale",centrale)
        self.render_figure.set_param("machinealavercentrale",machinealaver)
        return self.render_figure.render_figure("welcome/index.html")
    def voirtouteslesmachinealaver(self,search):
        try:
            myid=search["myid"][0]
        except:
            myid=None
        print("hey")
        centrale=self.dbCentrale.getbyid(myid)
        print("centrale")
        machinealaver=self.dbMachinealaver.getallbycentraleid(myid)
        print("machinealaver")
        self.render_figure.set_param("centrale",centrale)
        self.render_figure.set_param("machinealavercentrale",machinealaver)
        return self.render_figure.render_figure("welcome/index.html")
    def run(self,redirect=False,redirect_path=False,path=False,session=False,params={},url=False,post_data=False):
        if post_data:
            self.set_post_data(post_data)
        if url:
            print("url : ",url)
            self.Program.set_url(url)
        self.set_my_session(session)

        if redirect:
            self.redirect=redirect
        if redirect_path:
            self.redirect_path=redirect
        if not self.render_figure.partie_de_mes_mots(balise="section",text=self.Program.get_title()):
            self.render_figure.ajouter_a_mes_mots(balise="section",text=self.Program.get_title())
        if path and path.endswith("jpg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith(".jfif"):
            self.Program=Pic(path)
        elif path and path.endswith(".css"):
            self.Program=Css(path)
        elif path and path.endswith(".js"):
            self.Program=Js(path)
        elif path:
            print("link route ",path)
            ROUTES={

                    '^/$': self.voirtouteslesmachinealaver,
                    '^/machinealaver$': self.machinealaver,
                    }
            REDIRECT={"/save_user": "/welcome"}
            for route in ROUTES:
               print("pattern=",route)
               mycase=ROUTES[route]
               x=(re.match(route,path))
               print(True if x else False)
               if x:
                   params["routeparams"]=x.groups()
                   try:
                       self.Program.set_html(html=mycase(params))


                   except Exception:  
                       self.Program.set_html(html="<p>une erreur s'est produite "+str(traceback.format_exc())+"</p><a href=\"/\">retour à l'accueil</a>")
                   self.Program.redirect_if_not_logged_in()
                   return self.Program
               else:
                   self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")
        return self.Program
