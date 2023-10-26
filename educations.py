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
