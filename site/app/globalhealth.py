#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import os

urls = ( '/', 'index')

#app = web.application(urls, globals()) 

cur_path = os.path.dirname(os.path.abspath(__file__))
up_path = os.path.dirname(cur_path)

render = web.template.render(up_path+'/template/')

translations={
"Email": ["Email", "邮件"],
"Password":["Password", '请输入密码']    
}
class conf(object):
    def __init__(self):
        self.title = "Default"
        self.web = web
    def tr(self, s):
        if translations.has_key(s) :
            return translations[s][1]
        else:
            return  s        

class index(object):
    def GET(self):
        ctx = conf()
        return render.index(ctx)


if __name__ == "__main__":
    app = web.application(urls, globals())
    web.wsgi.runwsgi = lambda func, addr = None: web.wsgi.runfcgi(func, addr)
    app.run()

#if __name__ =="__main__":
#    #app = web.application(urls, globals())
#    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
#    app.run()


