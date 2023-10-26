import sqlite3
import sys
class Jobs():
        def __init__(self):
             self.con=sqlite3.connect("myFile.db")
             self.cur=self.con.cursor()
             self.cur.execute("create table jobs if not exists(
             id integer primary key,
             user_id integer,
             university text,
             city text,
             job text,
             begin date,
             end date

             );")
             print(self.mydb)
        def createmany(self,myid,mylist):
            for x in mylist:
                x["user_id"] = myid
                self.cur.execute("insert into jobs (user_id, university, city, job, begin, end) values (:user_id, :university, :city, :job, :begin, :end)",x)
        def updatemany(self,myid,mylist):
            ids=[myid]
            myvars=[]
            for x in mylist:
                self.cur.execute("update jobs set user_id = :user_id, university = :university, city = :city, begin = :begin, end = :end where id = :id",x)
                myvars.append("?")
                ids.append(x["id"])
            if len(mylist) > 0:
                self.cur.execute("delete from jobs where user_id = ? and id not in ("+"".join(myvars)+")", ids)
            else:
                self.cur.execute("delete from jobs where user_id = ?", ids)
