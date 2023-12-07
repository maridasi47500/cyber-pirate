# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from requests import get
class Myipaddress(Model):
    def __init__(self):
        self.ip="127.0.0.1"
    def get(self):
        self.ip=get('https://api.ipify.org').content.decode('utf8')
        return 'Mon adresse IP publique est: {}.'.format(self.ip)
