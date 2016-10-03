#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import os

urls = ( '/', 'index')

#app = web.application(urls, globals()) 

cur_path = os.path.dirname(os.path.abspath(__file__))
up_path = os.path.dirname(cur_path)

render = web.template.render(up_path+'/template/')

class index(object):
    def GET(self):
        return render.index(None)


if __name__ == "__main__":
    app = web.application(urls, globals())
    web.wsgi.runwsgi = lambda func, addr = None: web.wsgi.runfcgi(func, addr)
    app.run()

#if __name__ =="__main__":
#    #app = web.application(urls, globals())
#    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
#    app.run()


