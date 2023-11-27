# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Centrale(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists centrale(
        id integer primary key autoincrement,
        nom text
                    );""")

        self.con.commit()
        self.cur.execute("insert or ignore into centrale (nom) values (:nom)",{"nom":"ma laverie"})
        self.con.commit()
    def getall(self):
        self.cur.execute("select * from centrale")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from centrale where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid = 0):
        self.cur.execute("select * from centrale where id = ?",(myid,))
        try:
          row=dict(self.cur.fetchone())
        except:
          row={}
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
          self.cur.execute("insert into centrale (nom) values (:nom)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["centrale_id"]=myid
        azerty["notice"]="votre centrale a été ajouté"
        return azerty




