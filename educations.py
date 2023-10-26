import sqlite3
import sys
class Educations():
        def __init__(self):
             self.con=sqlite3.connect("myFile.db")
             self.cur=self.con.cursor()
             self.cur.execute("create table educations if not exists(
             id integer primary key,
             user_id integer,
             university text,
             diploma text,
             faculty text,
             department text,
             begin date,
             end date

             );")
             print(self.mydb)
        def createmany(self,myid,mylist):
            for x in mylist:
                x["user_id"] = myid
                self.cur.execute("insert into educations (user_id, university, diploma, faculty, department, begin, end) values (:user_id, :university, :diploma, :faculty, :department, :begin, :end)",x)
        def updatemany(self,myid,mylist):
            ids=[myid]
            myvars=[]
            for x in mylist:
                myvars.append("?")
                ids.append(x["id"])
                self.cur.execute("update educations set user_id = :user_id, university = :university, diploma = :diploma, faculty = :faculty, department = :department, begin = :begin, end = :end where id = :id",x)
            if len(mylist) > 0:
                self.cur.execute("delete from educations where user_id = ? and id not in ("+",".join(myvars)+")")
            else:
                self.cur.execute("delete from educations where user_id = ?",ids)
