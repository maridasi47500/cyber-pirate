class Directory():
    def __init__(self, title):
        self.title=title
        self.path="./"
        self.html=""
        self.redirect=False
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
