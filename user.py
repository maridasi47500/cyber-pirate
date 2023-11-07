import sqlite3
import sys
from researchfocus import Researchfocus
from jobs import Jobs
from educations import Educations
import re
from model import Model
class User(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists users(
        id integer primary key autoincrement,
        mypic string,
        metier string,
        nomcomplet string,
        gender string,
        almamater string,
        educationlevel string,
        degree string,
        status string,
        school string,
        discipline string,
        businessaddress string,
        postaladdress string,
        email string,
        profile text,
        zipcode string,
        otheremail string,
        password string
                );""")
        self.con.commit()
        #self.con.close()
    def getbyemailpw(self,email,pw):
        self.cur.execute("select * from users where otheremail = ? and password = ?",(email,pw,))

        
        row=self.cur.fetchone()
        print(dict(row))
        print(row)
        if row:
            return {"notice":"vous êtes connecté","name": row["nomcomplet"],"email": row["otheremail"]}
        else:
            return {"notice":None,"name":None,"email": None}
    def getall(self):
        self.cur.execute("select * from users")
        
        row=self.cur.fetchall()
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from users where id = ?",(myid,))
        
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")

        self.cur.execute("select * from educations where user_id = ?",(myid,))
        educations=self.cur.fetchall()
        row["educations"]=educations

        self.cur.execute("select * from researchfocus where user_id = ?",(myid,))
        res=self.cur.fetchall()
        row["researchfocus"]=res
        self.cur.execute("select * from jobs where user_id = ?",(myid,))
        job=self.cur.fetchall()
        row["jobs"]=job
        return row
    def create(self,params):
        #self.con=sqlite3.connect(self.mydb)
        print("ok")
        myhash={}
        myeducations=[]
        myjobs=[]

        focus={}
        education={}
        myfocus=[]
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[content]' in x and "focus" in x:
                thisid=x.split("focus][")[1].split("]")[0]
                mykey="researchfocus"
                content="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="content")
                job={"content": params[content][0]}
                myfocus.append(job)
            if '[university]' in x and "[educations]" in x:
                thisid=x.split("educations][")[1].split("]")[0]
                mykey="educations"
                uni="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="university")
                department="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="dep")
                faculty="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="faculty")
                diploma="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="diploma")
                mybegin="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="begin")
                myend="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="end")
                job={"university": params[uni][0], "end": params[myend][0], "begin": params[mybegin][0], "diploma": params[diploma][0],"faculty": params[faculty][0], "university": params[uni][0], "dep": params[department][0]}
                myeducations.append(job)
            if '[university]' in x and "[jobs]" in x:
                thisid=x.split("jobs][")[1].split("]")[0]
                namejob="user[jobs][{myid}][job]".format(myid=thisid)
                unijob="user[jobs][{myid}][university]".format(myid=thisid)
                cityjob="user[jobs][{myid}][city]".format(myid=thisid)
                beginjob="user[jobs][{myid}][begin]".format(myid=thisid)
                endjob="user[jobs][{myid}][begin]".format(myid=thisid)
                job={"job": params[namejob][0], "end": params[endjob][0], "begin": params[beginjob][0], "city": params[cityjob][0], "university": params[unijob][0]}
                myjobs.append(job)
            if '[' not in x and x not in ['routeparams']:
                print("my params",x,params[x])
                myhash[x]=params[x][0]
        print(myhash)
        self.cur.execute("insert into users (postaladdress,metier,mypic,nomcomplet,gender, almamater, educationlevel, degree, status, school, discipline, businessaddress, email, profile, zipcode, otheremail, password) values (:postaladdress,:metier,:mypic,:nomcomplet,:gender, :almamater, :educationlevel, :degree, :status, :school, :discipline, :businessaddress, :email, :profile, :zipcode, :otheremail, :password)",myhash)
        
        self.cur.execute("select id,otheremail,name from users where password = ? and email = ?", [myhash["password"], myhash["email"]])
        row=self.cur.fetchone()
        
        myid=row["id"]
        self.con.commit()
        print("my row id", myid)
        educations=Educations().createmany(myid=myid,mylist=myeducations)
        focuss=Researchfocus().createmany(myid=myid,mylist=myfocus)
        jobs=Jobs().createmany(myid=myid,mylist=myjobs)
        arr=educations+focuss+jobs
        #print(arr, "my array")
        for a,b in arr:
            print(a,b)
            self.cur.execute(a,b)
        self.con.commit()
        return {"notice": "vous avez été inscrit(e)","email": row["otheremail","name":row["nomcomplet"]]}


    def update(self,params):
        #self.con=sqlite3.connect(self.mydb)
        print("ok")
        myhash={}
        myeducations=[]
        myjobs=[]

        focus={}
        education={}
        myfocus=[]
        for x in params:
            if 'envoyer' in x:
                continue
            if 'confirmation' in x:
                continue
            if '[id]' in x and "focus" in x:
                thisid=x.split("jobs][")[1].split("]")[0]
                mykey="researchfocus"
                focus_id="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="id")
                content="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="content")
                job={"content": params[content][0], "id": params[focus_id][0]}
                myfocus.append(job)
            if '[id]' in x and "[educations]" in x:
                thisid=x.split("jobs][")[1].split("]")[0]
                mykey="educations"
                uni="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="university")
                department="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="dep")
                faculty="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="faculty")
                diploma="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="diploma")
                mybegin="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="begin")
                myend="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="end")
                job_id="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="id")
                job={"id": params[job_id][0],"university": params[uni][0], "end": params[myend][0], "begin": params[mybegin][0], "diploma": params[diploma][0],"faculty": params[faculty][0], "university": params[school][0]}
                myeducations.append(job)
            if '[id]' in x and "[jobs]" in x:
                mykey="jobs"
                thisid=x.split("jobs][")[1].split("]")[0]
                namejob="user[jobs][{myid}][job]".format(myid=thisid)
                unijob="user[jobs][{myid}][university]".format(myid=thisid)
                cityjob="user[jobs][{myid}][city]".format(myid=thisid)
                beginjob="user[jobs][{myid}][begin]".format(myid=thisid)
                idjob="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid, mykey=mykey, myotherkey="id")
                job={"id": params[idjob][0],"job": params[namejob][0], "end": params[endjob][0], "begin": params[beginjob][0], "city": params[cityjob][0], "university": params[unijob][0]}
                myjobs.append(job)
            if '[' not in x:
                myhash[x]=params[x][0]
        self.cur.execute("update users set postaladdress = :postaladdress,mypic = :mypic,nomcomplet = :nomcomplet,gender = :gender, almamater = :almamater, educationlevel = :educationlevel, degree = :degree, status = :status, school = :school, discipline = :discipline, businessaddress = :businessaddress, email = :email, profile = :profile, zipcode = :zipcode, otheremail = :otheremail, password = :password where id = :id",myhash)
        self.con.commit()
        myid=myhash["id"]
        educations=Educations()
        educations=educations.updatemany(myid=myid,mylist=myeducations)
        researchfocuss=Researchfocus()
        researchfocuss=researchfocuss.updatemany(myid=myid,mylist=myfocus)
        jobs=Jobs()
        jobs=jobs.updatemany(myid=myid,mylist=myjobs)
        arr=educations+researchfocuss+jobs
        print(arr, "my array")
        for a,b in arr:
            print(a,b)
            self.cur.execute(a,b)
            self.con.commit()
        return {"email": row["email"]}
