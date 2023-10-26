import sqlite3
import sys
class Researchfocus():
        def __init__(self):
             self.con=sqlite3.connect("myFile.db")
             self.cur=self.con.cursor()
             self.cur.execute("create table researchfocus if not exists(
             id integer primary key,
             user_id integer,
             content text,

             );")
             print(self.mydb)
        def createmany(self, myid, mylist):
            for x in mylist:
                x["user_id"] = myid
                self.cur.execute("insert into researchfocus (user_id, content) values (:user_id, :content)")
        def updatemany(self, myid, mylist):
            ids=[myid]
            myvars=[]
            for x in mylist:
                self.cur.execute("update researchfocus set user_id = :user_id, content = :content where id = :id", x)
                ids.append(x["id"])
                myvars.append("?")
            if len(mylist) > 0:
                self.cur.execute("delete from researchfocus where user_id = ? and id not in("+",".join(myvars)+")", ids)
            else:
                self.cur.execute("delete from researchfocus where user_id = ?", ids)

