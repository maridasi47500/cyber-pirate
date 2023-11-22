from directory import Directory
from render_figure import RenderFigure
from user import User
from news import News
from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.Program=Directory("mon petit guide de python")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.dbUsers=User()
        self.dbNews=News()
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
    def logout(self,search):
        self.Program.logout()
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def login(self,s):
        search=self.get_post_data()(params=("email","password"))
        self.user=self.dbUsers.getbyemailpw(search["email"],search["password"])
        print("user trouve", self.user)
        if self.user["email"]:
          self.set_session(self.user)
          self.set_session(self.user)
          self.set_json("{\"redirect\":\"/welcome\"}")
        else:
          self.set_json("{\"redirect\":\"/\"}")
        print("session login",self.Program.get_session())
        return self.render_figure.render_json()
    def new(self,search):
        return self.render_figure.render_figure("news/new.html")
    def createnew(self,params={}):
        myparams=self.get_post_data()(params=("content",))
        self.user=self.dbNews.create(myparams)
        if self.user["news_id"]:
          self.set_notice(self.user["notice"])
          self.set_json("{\"redirect\":\"/seemynews/"+self.user["news_id"]+"\"}")
        else:
          self.set_json("{\"redirect\":\"/new\"}")
        return self.render_figure.render_json()
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def delete_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(self.getparams)
        self.render_figure.set_param("user",User().deletebyid(myparam["id"]))
        self.set_redirect("/welcome")
        return self.render_figure.render_redirect()
    def edit_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(getparams)
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/edituser.html")
    def seenew(self,params={}):
        getparams=("id",)
        myparam=self.post_data(getparams)
        self.render_figure.set_param("news",News().getbyid(myparam["id"]))
        return self.render_figure.render_figure("news/shownews.html")
    def seeuser(self,params={}):
        getparams=("id",)
        myparam=self.post_data(getparams)
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/showuser.html")
    def mynews(self,params={}):
        self.render_figure.set_param("mynews",News().getall())
        return self.render_figure.render_figure("news/allnews.html")
    def myusers(self,params={}):
        self.render_figure.set_param("users",User().getall())
        return self.render_figure.render_figure("welcome/users.html")
    def set_post_data(self,x):
        self.post_data=x
    def get_post_data(self):
        return self.post_data
    def update_user(self,params={}):
        myparam=self.post_data(self.getparams)
        self.user=self.dbUsers.update(params)
        self.set_session(self.user)
        self.set_redirect(("/seeuser/"+params["id"][0]))
        return self.render_figure.render_redirect()
    def save_user(self,params={}):
        #print("My  f unc",self.post_data)
        myparam=self.get_post_data()(params=("businessaddress","gender","profile","metier", "otheremail", "password","zipcode", "email", "mypic","postaladdress","nomcomplet","password_confirmation"))
        #print("My p  a r a m",myparam)
        self.user=self.dbUsers.create(myparam)
        if self.user["email"]:
          self.set_session(self.user)
          self.set_json("{\"redirect\":\"/welcome\"}")
          return self.render_figure.render_json()
        else:
          self.set_json("{\"redirect\":\"/e\"}")
          return self.render_figure.render_json()
    def data_reach(self,search):
        return self.render_figure.render_figure("welcome/datareach.html")
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
                    "^/allmynews$":self.mynews,
                    '^/logmeout$':self.logout,
                    '^/save_user$':self.save_user,
                    '^/update_user$':self.update_user,
                    '^/new$':self.new,
                    '^/createnew$':self.createnew,

                    "^/seemynews/([0-9]+)$":self.seenew,
                    "^/seeuser/([0-9]+)$":self.seeuser,
                    "^/edituser/([0-9]+)$":self.edit_user,
                    "^/deleteuser/([0-9]+)$":self.delete_user,
                    '^/login$':self.login,

                    '^/welcome$':self.myusers,

                    '^/$': self.welcome,
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
