import re
import os
class RenderFigure():
    def __init__(self,program):
        self.mytemplate="./mypage/index.html"
        self.path=program.get_path()
        self.title=program.get_title()
        self.headingone=program.get_title()
        self.body=""
        self.params={}
    def set_param(self,x,y):
        self.params[x]=y
    def render_collection(self, collection,partial,as):
        myview=open(os.path.abspath(+"./"+partial),"r").read()
        mystr=""
        for x in collection:
            for j in myview.split("<%="):
                if "%>" not in j:
                    mystr+=j
                    continue

                k=j.split("%>")
                loc={"render_collection": self.render_collection,as: x  "params": self.params}
                l=exec("myvalue="+k[0], globals(), loc)
                mystr+=loc["myvalue"]
                mystr+=k[1]
        return mystr
    def partie_de_mes_mots(self,balise="",text=""):
        r="<{balise}>{text}</{balise}>"
        s="""
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(debutmots=self.title, mot=self.headingone,plusdemots=self.body)
        return re.search(r, s)
    def debut_de_mes_mots(self,balise="div",text=""):
        r="<{balise}>{text}</{balise}>"
        s="""
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(debutmots=self.title, mot=self.headingone,plusdemots=self.body)
        return re.match(r, s)
    def fin_de_mes_mots(self,balise="div",text=""):
        r="<{balise}>{text}</{balise}>$"
        s="""
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(mot=self.headingone,plusdemots=self.body)
        return re.search(r, s)
    def ajouter_a_mes_mots(self,balise,text):
        r="<{balise}>{text}</{balise}>".format(balise=balise,text=text)
        self.body+=r

    def render_figure(self,filename):
        
        self.body+=open(os.path.abspath(self.path+"/"+filename),"r").read()
        return open(os.path.abspath(self.mytemplate),"r").read().format(debutmots=self.title, mot=self.headingone,plusdemots=self.body)
