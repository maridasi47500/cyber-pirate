import sqlite3
import sys
import re
from model import Model
class News(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists news(
        id integer primary key autoincrement,
        content text);""")
        self.con.commit()
    def getall(self):
        self.cur.execute("select * from news")
        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):
        self.cur.execute("delete from news where id = ?",(myid,))
        

        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from news where id = ?",(myid,))
        
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")

        job=self.cur.fetchall()

        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'submit' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                print("my params",x,params[x])
                myhash[x]=params[x]
        print("CECI EST MON H A SH")
        print(myhash)
        try:
          self.cur.execute("insert into news (content) values (:content)",myhash)
          self.con.commit()
        except Exception as e:
          print("my error"+str(e))
        

        #print(arr, "my array")
        self.con.commit()
        myid=self.cur.lastrowid
        

        print("my row id", myid)
        return {"notice": "vous avez créé une news","news_id": str(myid)}


    def update(self,params):
        #self.con=sqlite3.connect(self.mydb)
        print("ok")
        myhash={}
        for x in params:
            if 'submit' in x:
                continue
            if 'envoyer' in x:
                continue
            if 'confirmation' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                print(x)

                print(params[x])
                myhash[x]=params[x][0]
        try:
          self.cur.execute("update users set postaladdress = :postaladdress,mypic = :mypic,nomcomplet = :nomcomplet,gender = :gender, businessaddress = :businessaddress, email = :email, profile = :profile, zipcode = :zipcode, otheremail = :otheremail, password = :password where id = :id",myhash)
          self.con.commit()
        except Exception as e:
          print("my error update"+str(e))
        myid=myhash["id"]
        #print(arr, "my array")
        self.cur.execute("select id,otheremail,nomcomplet from users where id = ?", (myid,))
        row=self.cur.fetchone()
        return {"notice": "vos infos ont été modifiées","email": row["otheremail"],"name":row["nomcomplet"]}
