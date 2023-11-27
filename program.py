# coding=utf-8
import sqlite3
import sys
import re
import datetime
from model import Model
class Program(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists program(
        id integer primary key autoincrement,
        machinealaver_id text,
            mydatetime datetime
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from program")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from program where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from program where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def createwithmachinealaverid(self,machinealaverid):
        print("ok")
        myid=None
        now=datetime.datetime.now()
        myhash={"machinealaver_id":machinealaverid, "mydatetime": now}
        somevalue=(machinealaverid, now,)
        cherche=self.cur.execute("select * from program where machinealaver_id = ? and datetime(mydatetime,'+45 minutes') > ?",somevalue)
        mycherche=self.cur.fetchall()
        try:
          if len(mycherche) == 0:
            self.cur.execute("insert into program (machinealaver_id,mydatetime) values (:machinealaver_id,:mydatetime)",myhash)
            self.con.commit()
            myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        cherche=self.cur.execute("select * from program where machinealaver_id = ? and datetime(mydatetime,'+45 minutes') > ?",somevalue)
        mycherche=self.cur.fetchall()
        myid=str(self.cur.lastrowid)
        azerty={}
        azerty["program_id"]=myid
        azerty["notice"]="votre program a été ajouté"
        return azerty
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
          self.cur.execute("insert into program (machinealaver_id,mydatetime) values (:machinealaver_id,:mydatetime)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["program_id"]=myid
        azerty["notice"]="votre program a été ajouté"
        return azerty




