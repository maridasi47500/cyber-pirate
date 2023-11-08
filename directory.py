class Directory():
    session=False
    def __init__(self, title):
        self.title=title
        self.session={"email":None,"name":None,"notice":None}
        self.path="./"
        self.html=""
        self.url=""
        self.redirect=False
    def logout(self):
        for x in ["email","name","notice"]:
            try:
                self.session[x]=""
            except:
                print("erreur session logout ",x)
                self.session[x]=""
        self.session["mysession"]=True
    def not_notice(self):
        self.session["notice"]=""
    def get_session(self):
        return self.session
    def set_my_session(self,s):
        for x in ["email","name","notice"]:
            try:
                self.session[x]=s[x]
            except:
                print("erreur session ",x)
                self.session[x]=""
        self.session["mysession"]=False
    def set_session(self,s):
        for x in ["email","name","notice"]:
            try:
                self.session[x]=s[x]
            except:
                print("erreur session ",x)
                self.session[x]=""
        self.session["mysession"]=True
    def get_url(self):
        return self.url
    def set_url(self,url):
        self.url=url
    def get_html(self):
        return self.html
    def set_html(self,html):
        self.html=html
    def set_redirect(self,red):
        self.redirect=red
        self.html="Moved permanently to <a href=\"{url}\">{url}</a>".format(url=red)
    def get_redirect(self):
        return self.redirect
    def set_path(self,path):
        self.path=path
    def get_title(self):
        return self.title
    def get_path(self):
        return self.path
    def redirect_if_not_logged_in(self):
        mysession=self.get_session()
        print("url : : ",self.url)
        print("session : : ",mysession)
        if not mysession["mysession"]:
            self.session["notice"]=""
        if (not mysession or (not mysession["email"] and not mysession["name"])) and self.url != "/" and not self.redirect:
            print("ok not loged in")
            redi="/"
            self.redirect=redi
            self.html="Moved permanently to <a href=\"{url}\">{url}</a>".format(url=redi)
            self.session["notice"]="vous n'êtes pas connecté"
