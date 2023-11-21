#!/usr/bin/env python3
"""
License: MIT License
Copyright (c) 2023 Miel Donkers

Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from route import Route
from urllib import parse
from urllib.parse import parse_qs, urlparse
import requests
req = requests.Session()
req.cookies["email"]=""
req.cookies["name"]=""
req.cookies["notice"]=""
from urllib.parse import urlencode
class S(BaseHTTPRequestHandler):
    def deal_post_data(self,params):
        try:
            print("MY P.A.R.A.M.S",params,self.headers.keys())
            content_type = self.headers['Content-Type']
            myhash={}
            if not content_type:
                print(False, "Content-Type header doesn't contain boundary")
                return (False, "Content-Type header doesn't contain boundary")
            boundary = content_type.split("=")[1].encode()
            remainbytes = int(self.headers['Content-Length'])
            line = self.rfile.readline()
            remainbytes -= len(line)
            if not boundary in line:
                print(False, "Content NOT begin with boundary")
                return (False, "Content NOT begin with boundary")
            line = self.rfile.readline()
            remainbytes -= len(line)
            for param in params:
                print("P a r a m : ",param)
                fn = re.findall(r'Content-Disposition.*name="'+param+'"; filename="(.*)"', line.decode())
                if not fn:
                    n = re.findall(r'Content-Disposition.*name="'+param+'"', line.decode())
                    path = self.translate_path(self.path)
                    n = n[0]
                    line = self.rfile.readline()
                    remainbytes -= len(line)
                    line = self.rfile.readline()
                    remainbytes -= len(line)
                    try:
                        content = ""
                    except IOError:
                        #return (False, "Can't create file to write, do you have permission to write?")
                        print(False, "Can't create file to write, do you have permission to write?")
                        continue
                    preline = self.rfile.readline()
                    remainbytes -= len(preline)
                    while remainbytes > 0:
                        line = self.rfile.readline()
                        remainbytes -= len(line)
                        if boundary in line:
                            preline = preline[0:-1]
                        if preline.endswith(b'\r'):
                            preline = preline[0:-1]
                            content+=write(preline)
                            myhash[param]=content
                            print(True, "File '%s' upload success!" % n)
                            break#return (True, "File '%s' upload success!" % fn)
                        else:
                            content+=preline
                            preline = line
                    print(False, "Can't find out file name...")
                #path = self.translate_path(self.path)
                path="./uploads"
                fn = os.path.join(path, fn[0])
                line = self.rfile.readline()
                remainbytes -= len(line)
                line = self.rfile.readline()
                remainbytes -= len(line)
                try:
                    out = open(fn, 'wb')
                except IOError:
                    print(False, "Can't create file to write, do you have permission to write?")
                    continue#return (False, "Can't create file to write, do you have permission to write?")
                preline = self.rfile.readline()
                remainbytes -= len(preline)
                while remainbytes > 0:
                    line = self.rfile.readline()
                    remainbytes -= len(line)
                    if boundary in line:
                        preline = preline[0:-1]
                    if preline.endswith(b'\r'):
                        preline = preline[0:-1]
                        out.write(preline)
                        out.close()
                        myhash[param] = fn
                        print(True, "File '%s' upload success!" % fn)
                        break#return (True, "File '%s' upload success!" % fn)
                    else:
                        out.write(preline)
                        preline = line
            #return (False, "Unexpect Ends of data.")
            print(False, "Unexpect Ends of data.")
        except Exception as e:
            print(e,"my exception")
        return myhash
    def _set_response(self,redirect=False,cookies=False,pic=False,js=False):
        if redirect:
          self.send_response(301)
          self.send_header('Status', '301 Redirect')
          self.send_header('Location', redirect)
          self.send_header('Content-type', 'text/html;charset=utf-8')
        elif js:
          self.send_response(200)
          self.send_header('Content-type', 'text/javascript')
        elif pic:
          self.send_response(200)
          self.send_header('Content-type', 'image/'+pic)
        else:
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
        if cookies:
          self.send_header("Cookie", urlencode(cookies))

        self.end_headers()
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        myparams = parse_qs(urlparse(self.path).query)
        dictcook=(req.cookies.get_dict())

        myProgram=Route().run(path=str(self.path),params=myparams,session=dictcook,url=self.path,post_data=False)
        sess= myProgram.get_session()
        print("param session",sess)
        if sess:
            for cookie in req.cookies:
                    cookie.value = sess[cookie.name]

        self._set_response(redirect=myProgram.get_redirect(),cookies=req.cookies,pic=myProgram.get_pic(),js=myProgram.get_js())
        self.wfile.write(myProgram.get_html())
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        #post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), "post data")
        myparams = parse_qs(urlparse(self.path).query)
        dictcook=(req.cookies.get_dict())
        print("d i ct cook",dictcook)
        print("p a r a m s",myparams)


        #logging.info(parse.parse_qs(post_data.decode('utf-8')))
        myProgram=Route().run(path=str(self.path),params=myparams,session=dictcook,url=self.path,post_data=self.deal_post_data)
        sess= myProgram.get_session()
        if sess:
          for x in sess:
            req.cookies.set(x,sess[x])

        self._set_response(redirect=myProgram.get_redirect(),cookies=req.cookies,pic=myProgram.get_pic(),js=myProgram.get_js())
        self.wfile.write(myProgram.get_html().encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
