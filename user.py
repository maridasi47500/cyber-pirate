import sqlite3
import sys
from researchfocus import Researchfocus
from jobs import Jobs
from educations import Educations
import re
class User():
    def __init__(self):
        self.con=sqlite3.connect("myFile.db")
        self.cur=self.con.cursor()
        self.cur.execute("create table users if not exists(
        id integer primary key,
        mypic string,
        nomcomplet string,
        gender string,
        almamater string,
        educationlevel string,
        degree string
        status string,
        school string,
        discipline string,
        businessaddress string,
        email string,
        personalprofile string,
        zipcode string,
        otheremail string,
        password string,






                );")
        print(self.mydb)
    def create(self,params):
        print("ok")
        myhash={}
        myeducations=[]
        myjobs=[]

        focus={}
        education={}
        myfocus=[]
        for x in params:
            if '[id]' in x and "focus" in x:
                thisid=x.split("jobs][")[1].split("]")[0]
                mykey="researchfocus"
                content="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="content")
                job={"content": params[content][0]}
                myfocus.append(job)
            if '[id]' in x and "[educations]" in x:
                thisid=x.split("jobs][")[1].split("]")[0]
                mykey="educations"
                uni="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="university")
                department="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="department")
                faculty="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="faculty")
                diploma="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="diploma")
                mybegin="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="begin")
                myend="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="end")
                job={"university": params[uni][0], "end": params[myend][0], "begin": params[mybegin][0], "diploma": params[diploma][0],"faculty": params[faculty][0], "university": params[school][0]}
                myeducations.append(job)
            if '[id]' in x and "[jobs]" in x:
                thisid=x.split("jobs][")[1].split("]")[0]
                namejob="user[jobs][{myid}][job]".format(myid=thisid)
                unijob="user[jobs][{myid}][university]".format(myid=thisid)
                cityjob="user[jobs][{myid}][city]".format(myid=thisid)
                beginjob="user[jobs][{myid}][begin]".format(myid=thisid)
                endjob="user[jobs][{myid}][begin]".format(myid=thisid)
                job={"job": params[namejob][0], "end": params[endjob], "begin": params[beginjob], "city": params[cityjob], "university": params[unijob]}
                myjobs.append(job)
            if '[' not in x:
                myhash[x]=params[x][0]
        cur.execute("insert into users (mypic,nomcomplet,gender, almamater, educationlevel, degree, status, school, discipline, businessaddress, email, personalprofile, zipcode, otheremail, password) values (:mypic,:nomcomplet,:gender, :almamater, :educationlevel, :degree, :status, :school, :discipline, :businessaddress, :email, :personalprofile, :zipcode, :otheremail, :password)",myhash)
        user=self.cur.execute("select id from users where password = ? and email = ?", [myhash["password"], myhash["email"]])
        row=cur.fetchone()
        myid=row["id"]
        educations=Educations().createmany(myid=myid,myeducations)
        educations=Researchfocus().createmany(myid=myid,myfocus)
        jobs=Jobs().createmany(myid=myid,myjobs)
    def update(self,params):
        print("ok")
        myhash={}
        myeducations=[]
        myjobs=[]

        focus={}
        education={}
        myfocus=[]
        for x in params:
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
                department="user[{mykey}][{myid}][{myotherkey}]".format(myid=thisid,mykey=mykey,myotherkey="department")
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
                job={"id": params[idjob][0],"job": params[namejob][0], "end": params[endjob], "begin": params[beginjob], "city": params[cityjob], "university": params[unijob]}
                myjobs.append(job)
            if '[' not in x:
                myhash[x]=params[x][0]
        cur.execute("update users set mypic = :mypic,nomcomplet = :nomcomplet,gender = :gender, almamater = :almamater, educationlevel = :educationlevel, degree = :degree, status = :status, school = :school, discipline = :discipline, businessaddress = :businessaddress, email = :email, personalprofile = :personalprofile, zipcode = :zipcode, otheremail = :otheremail, password = :password where id = :id",myhash)
        myid=myhash["id"]
        educations=Educations().updatemany(myid=myid,myeducations)
        educations=Researchfocus().updatemany(myid=myid,myfocus)
        jobs=Jobs().updatemany(myid=myid,myjobs)
