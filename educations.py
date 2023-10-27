import sqlite3
import sys
from model import Model
class Educations(Model):
        def __init__(self):
             self.con=sqlite3.connect(self.db)
             self.cur=self.con.cursor()
             self.cur.execute("""create table if not exists educations(
             id integer primary key autoincrement,
             user_id integer,
             university text,
             diploma text,
             faculty text,
             department text,
             begin date,
             end date

             );""")
             self.con.commit()

        def createmany(self,myid,mylist):
            print(mylist)
            for x in mylist:
                x["user_id"] = myid
                self.cur.execute("insert into educations (user_id, university, diploma, faculty, department, begin, end) values (:user_id, :university, :diploma, :faculty, :department, :begin, :end)",x)
                self.con.commit()
            self.con.close()
        def updatemany(self,myid,mylist):
            self.con=sqlite3.connect(self.db)
            ids=[myid]
            myvars=[]
            for x in mylist:
                myvars.append("?")
                ids.append(x["id"])
                self.cur.execute("update educations set user_id = :user_id, university = :university, diploma = :diploma, faculty = :faculty, department = :department, begin = :begin, end = :end where id = :id",x)
                self.con.commit()
            if len(mylist) > 0:
                self.cur.execute("delete from educations where user_id = ? and id not in ("+",".join(myvars)+")")
                self.con.commit()
            else:
                self.cur.execute("delete from educations where user_id = ?",ids)
                self.con.commit()
            self.con.close()
