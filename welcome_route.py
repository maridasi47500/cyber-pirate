from directory import Directory
from render_figure import RenderFigure
from route import Route
import re

class WelcomeRoute(Route):
    def __init__(self,path):
        self.path=path
        self.Program=Directory("mon petit guide de python")
        self.Program.set_path("./welcome")
        self.render_figure=RenderFigure(self.Program)
    def 
    def welcome(self,search):
        return self.render_figure.render_figure("welcome.html")
    def data_reach(self,search):
        return self.render_figure.render_figure("datareach.html")
