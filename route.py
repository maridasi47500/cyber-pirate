from directory import Directory
from render_figure import RenderFigure
from myscript import Myscript
from mycommandline import Mycommandline
from myipaddress import Myipaddress
from user import User

from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.Program=Directory("cyber pirate")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.ipaddress=Myipaddress()
        self.render_figure=RenderFigure(self.Program)
        self.getparams=("id",)
    def set_post_data(self,x):
        self.post_data=x
    def get_post_data(self):
        return self.post_data
    def set_my_session(self,x):
        print("set session",x)
        self.Program.set_my_session(x)
        self.render_figure.set_session(self.Program.get_session())
    def set_redirect(self,x):
        self.Program.set_redirect(x)
        self.render_figure.set_redirect(self.Program.get_redirect())
    def render_some_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_some_json(x)
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
        myparam=self.get_post_data()(params=("myid",))
        myid=myparam["myid"]
        print("hey")
        centrale=self.dbCentrale.getbyid(myid)
        print("centrale")
        print("machinealaver",centrale)
        machinealaver=self.dbMachinealaver.getallbycentraleid(myid)

        print("machinealaver",machinealaver)
        self.render_figure.set_param("centrale",centrale)
        self.render_figure.set_param("machinealaver",machinealaver)
        return self.render_some_json("welcome/machinealaver.json")
    def createuser(self,search):
        myparam=self.get_post_data()(params=("username","email","password","job",))
    def adresseip(self,search):
        maphrase=self.ipaddress.get()
        print(maphrase)
        self.render_figure.set_param("adresseip",maphrase)
        return self.render_some_json("welcome/adresseip.json")
    def ajouterimage(self,s):
        myparam=self.get_post_data()(params=("pic",))
        self.render_figure.set_param("pic",myparam["pic"])
        return self.render_some_json("welcome/pic.json")
    def hello(self,search):
        tags=[
        ["div","html","footer"],
        ["header","nav"]
        ]
        css=[
        ["display","color","background"],
        ["margin","padding"]
        ]
        phrases=[
                [{"nom":"mon adresse ip", "lien": "/myipaddress"}],
        []
        ]
        print(tags)
        self.render_figure.set_param("phrases",phrases)
        self.render_figure.set_param("tags",tags)
        self.render_figure.set_param("cssproprietes",css)
        print("tags")
        try:
            print(search["myid"])
            myid=search["myid"][0]
        except:
            myid=None
        return self.render_figure.render_figure("welcome/index.html")
    def run(self,redirect=False,redirect_path=False,path=False,session=False,params={},url=False,post_data=False):
        if post_data:
            print("post data")
            self.set_post_data(post_data)
            print("post data set",post_data)
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
            path=path.split("?")[0]
            print("link route ",path)
            ROUTES={

                    '^/ajouterimage$': self.ajouterimage,
                    '^/myipaddress$': self.adresseip,
                    '^/welcome$': self.createuser,
                    '^/$': self.hello,

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
                   return self.Program
               else:
                   self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")
        return self.Program
