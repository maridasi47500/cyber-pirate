from directory import Directory
class Pic(Directory):
    def __init__(self,name):
        self.name=name
        self.pic=name.split(".")[1]
        self.content=open("."+name, 'rb').read()
    def get_name(self):
        return self.name
    def get_html(self):
        return self.content
