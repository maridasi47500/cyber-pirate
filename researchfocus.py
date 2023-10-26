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
