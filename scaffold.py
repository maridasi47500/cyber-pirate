# -*- coding: utf-8 -*-

import sys
import os
print(sys.argv[1])


filename=sys.argv[1].lower()
myclass=(filename).capitalize()
modelname=(filename).capitalize()
marouteget="\"/%s\"" % filename
maroutenew="\"/%s_new\"" % filename
maroutecreate="\"/%s_create\"" % filename
marouteget2="\\\"/%s\\\"" % filename
myhtml="my"+filename+"html"
myfavdirectory=filename
index = 2 
createtable=""
columns="("
values="("
myparam=","
items=sys.argv
while index < (len(items)):

    try:
      print(index, items[index])
      paramname=items[index]
      print(items[(index+1)])
    except:
      myparam=""
    index += 1
    columns+="{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
    values+=":{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
    createtable+="""        {paramname} text{myparam}
    """.format(myparam=myparam,paramname=paramname)
columns+=")"
values+=")"
mystr="""# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class {modelname}(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute(\"\"\"create table if not exists {filename}(
        id integer primary key autoincrement,
"""
mystr+=createtable

mystr+="""                );\"\"\")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from {filename}")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

"""
mystr+="""        self.cur.execute("delete from {filename} where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from {filename} where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={myhash}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into {filename} {columns} values {values}",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={notice}
        azerty["{filename}_id"]=myid
        azerty["notice"]="votre {filename} a été ajouté"
        return azerty




"""
if not os.path.isfile(filename+".py"):
  f = open(filename+".py", "w") 
  res=(mystr.format(modelname=modelname,filename=filename,columns=columns,values=values,myhash={},notice={}))
  print(res)
  f.write(res)
  f.close()


with open("./route.py", "r") as f:
  contents = f.readlines()


#index=[i for i in range(len(contents)) if "class S(BaseHTTPRequestHandler):" in contents[i]][0]
#contents.insert(index, scriptfunc.format(myfavdirectory=myfavdirectory,myclass=filename,myhtml=myhtml))
#contents.insert(1, "global {myclass}\n".format(myclass=filename))
#contents.insert(1, "import {myclass}\n".format(myclass=filename))
#contents.insert(1, "from {myclass} import {myclass}page\n".format(myclass=filename))
#myrouteget="\"/{myclass}\":{myclass}func,\n"
#index=[i for i in range(len(contents)) if "myroutes = {" in contents[i]][0]
#contents.insert((index+1), myrouteget.format(myclass=filename))
#index=[i for i in range(len(contents)) if "def reloadmymodules" in contents[i]][0]
#contents.insert((index+1), "    reload({myclass})\n".format(myclass=filename))
#index=[i for i in range(len(contents)) if "__mots__={" in contents[i]][0]
#contents.insert((index+1), "    \"/{myclass}\":{\"partiedemesmots\":\"{myclass}\"},\n".replace("{myclass}",filename))

#with open("./script.py", "w") as f:
#    contents = "".join(contents)
#    f.write(contents)

#os.system("mkdir %s" % myfavdirectory)
#pathhtml="%s/%s.html" % (myfavdirectory, myhtml)
#os.system("touch %s" % pathhtml)

#if os.path.isfile(pathhtml):
#    with open(pathhtml, "w") as f:
#        urlayout="""<h1>Layout de la route {myclass}</h1>
#<p><a href="{marouteget}">nous sommes ici (essayez ce lien)</a></p>
#<p>Entrez du texte sur cette page</p>
#"""
#          f.write(urlayout.format(marouteget=marouteget,myclass=filename))
#
#  #print("ma route get %s a été ajoutée. Maintenant vous pouvez essayer d'y acceder" % marouteget)
