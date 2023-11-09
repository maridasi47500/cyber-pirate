import sqlite3
import sys
from model import Model
class Educations(Model):
        def __init__(self):
             #self.con=sqlite3.connect(self.db)
             #self.cur=self.con.cursor()
             self.arr=[]
             self.arr.append(["""create table if not exists educations(
             id integer primary key autoincrement,
             user_id integer,
             university text,
             diploma text,
             faculty text,
             dep text,
             begin date,
             end date

             );""",[]])
             #self.con.commit()

        def createmany(self,myid,mylist):
            print(mylist)
            for x in mylist:
                x["user_id"] = myid
                self.arr.append(["insert into educations (user_id, university, diploma, faculty, dep, begin, end) values (:user_id, :university, :diploma, :faculty, :dep, :begin, :end)",x])
                #self.con.commit()
            #self.con.close()
            return self.arr
        def updatemany(self,myid,mylist):
            #self.con=sqlite3.connect(self.db)
            ids=[myid]
            myvars=[]

                #self.con.commit()
            for x in mylist:
                x["user_id"] = myid

                try:
                  ids.append(x["id"])
                  myvars.append("?")
                  self.arr.append(["update educations set user_id = :user_id, university = :university, diploma = :diploma, faculty = :faculty, dep = :dep, begin = :begin, end = :end where id = :id",x])
                except:

                  self.arr.append(["insert into educations (user_id, university, diploma, faculty, dep, begin, end) values (:user_id, :university, :diploma, :faculty, :dep, :begin, :end)",x])
            if len(mylist) > 0:
                self.arr.insert(0,["delete from educations where user_id = ? and id not in ("+",".join(myvars)+")", ids])
                #self.con.commit()
            else:
                self.arr.insert(0,["delete from educations where user_id = ?",ids])
            return self.arr
