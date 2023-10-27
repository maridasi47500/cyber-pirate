import sqlite3
import sys
from model import Model
class Researchfocus(Model):
        def __init__(self):
             self.con=sqlite3.connect(self.db)
             self.cur=self.con.cursor()
             self.cur.execute("""create table if not exists researchfocus(
             id integer primary key autoincrement,
             user_id integer,
             content text

             );""")
             self.con.commit()
             #self.con.close()
        def createmany(self, myid, mylist):
            for x in mylist:
                x["user_id"] = myid
                self.cur.execute("insert into researchfocus (user_id, content) values (:user_id, :content)")
                self.con.commit()
            #self.con.close()
        def updatemany(self, myid, mylist):
            ids=[myid]
            myvars=[]
            for x in mylist:
                self.cur.execute("update researchfocus set user_id = :user_id, content = :content where id = :id", x)
                self.con.commit()
                ids.append(x["id"])
                myvars.append("?")
            if len(mylist) > 0:
                self.cur.execute("delete from researchfocus where user_id = ? and id not in("+",".join(myvars)+")", ids)
                self.con.commit()
            else:
                self.cur.execute("delete from researchfocus where user_id = ?", ids)
                self.con.commit()

            #self.con.close()
