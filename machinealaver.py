# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Machinealaver(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists machinealaver(
        id integer primary key autoincrement,
        nom text,
            etat text,
            centrale_id integer,
            num integer,
            UNIQUE(centrale_id, num) ON CONFLICT REPLACE

                    );""")
        self.con.commit()
        machinesalaver=[{"etat":"libre","num":"1","centrale_id":"1","nom":"machine a laver 5kg"}]
        machinesalaver.append({"etat":"libre","num":"2","centrale_id":"1","nom":"machine a laver 5kg"})
        machinesalaver.append({"etat":"libre","num":"3","centrale_id":"1","nom":"machine a laver 8kg"})
        machinesalaver.append({"etat":"libre","num":"4","centrale_id":"1","nom":"machine a laver 8kg"})
        machinesalaver.append({"etat":"libre","num":"5","centrale_id":"1","nom":"machine a laver 8kg"})
        machinesalaver.append({"etat":"libre","num":"6","centrale_id":"1","nom":"machine a laver 8kg"})
        machinesalaver.append({"etat":"libre","num":"7","centrale_id":"1","nom":"machine a laver 10kg"})
        machinesalaver.append({"etat":"libre","num":"8","centrale_id":"1","nom":"machine a laver 10kg"})
        machinesalaver.append({"etat":"libre","num":"9","centrale_id":"1","nom":"machine a laver 10kg"})
        machinesalaver.append({"etat":"libre","num":"10","centrale_id":"1","nom":"machine a laver 12kg"})
        machinesalaver.append({"etat":"libre","num":"11","centrale_id":"1","nom":"machine a laver 12kg"})
        machinesalaver.append({"etat":"libre","num":"12","centrale_id":"1","nom":"machine a laver 12kg"})
        for myhash in machinesalaver:
          self.cur.execute("insert or ignore into machinealaver (nom,etat,centrale_id,num) values (:nom,:etat,:centrale_id,:num)",myhash)
          self.con.commit()
    def getallbycentraleid(self,myid = 0):

        try:
          self.cur.execute("select machinealaver.id, machinealaver.nom, machinealaver.centrale_id, machinealaver.num, machinealaver.etat,program.mydatetime,centrale.heure_debut,centrale.heure_fin from machinealaver left outer join program on program.machinealaver_id = machinealaver.id left outer join centrale on centrale.id = machinealaver.centrale_id group by machinealaver.id having machinealaver.centrale_id = ?",(myid,))

          row=self.cur.fetchall()
        except Exception as e:
          print(e)
          row=[]
        return row
    def getall(self):
        self.cur.execute("select * from machinealaver")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from machinealaver where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from machinealaver where id = ?",(myid,))
        row=dict(self.cur.fetchone())
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
          self.cur.execute("insert into machinealaver (nom,etat,centrale_id,num) values (:nom,:etat,:centrale_id,:num)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["machinealaver_id"]=myid
        azerty["notice"]="votre machinealaver a été ajouté"
        return azerty




