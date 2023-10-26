class Directory():
    def __init__(self, title):
        self.title=title
        self.path="./"
        self.redirect=False
    def set_path(self,path):
        self.path=path
    def get_title(self):
        return self.title
    def get_path(self):
        return self.path
