import sqlite3
import sys
import re
from model import Model
class Storage(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists storages(
        id integer primary key autoincrement,
        name text,
        description text
                );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from storages")
        
        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):
        self.cur.execute("delete from storages where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from storages where id = ?",(myid,))
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
          self.cur.execute("insert into storages (name,description) values (:name,:description)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        
        #self.cur.execute("select id,name,description from storages where id = ?", (myid))
        #row=self.cur.fetchone()
        #
        #myid=row["id"]

        #print("my row id", myid)
        #print(arr, "my array")
        #self.con.commit()
        return {"notice": "votre stockage a été ajouté","storage_id":myid}


    def update(self,params):
        #self.con=sqlite3.connect(self.mydb)
        print("ok")
        myhash={}
        for x in params:
            if 'envoyer' in x:
                continue
            if 'confirmation' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                print(x)

                print(params[x])
                myhash[x]=params[x][0]
        try:
          self.cur.execute("update storages set postaladdress = :postaladdress,mypic = :mypic,nomcomplet = :nomcomplet,gender = :gender, businessaddress = :businessaddress, email = :email, profile = :profile, zipcode = :zipcode, otheremail = :otheremail, password = :password where id = :id",myhash)
          self.con.commit()
        except Exception as e:
          print("my error update"+str(e))
        myid=myhash["id"]
        #print(arr, "my array")
        self.cur.execute("select id,otheremail,nomcomplet from storages where id = ?", (myid,))
        row=self.cur.fetchone()
        return {"notice": "vos infos ont été modifiées","email": row["otheremail"],"name":row["nomcomplet"]}
