#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import os
import metroui

urls = ( '/[^/]*', 'index',
'/(.*)/(.*)', 'trsite',

)

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
        self.mui=metroui
        self.lang = 'zh-CN'
    def tr(self, s):
        if translations.has_key(s) :
            return translations[s][1]
        else:
            return  s        

class index(object):
    def GET(self, *args):
        ctx = conf()
        return render.index(ctx)


class trsite(object):
    def GET(self, lang, url):
        ctx=conf()
        ctx.lang = lang
        if ctx.lang not in ('zh-CN', 'en'):
            ctx.lang = 'zh-CN'
        if url == '':
            return render.index(ctx)
        elif url == 'start':
            return render.start(ctx)
        else:
            return render.index(ctx)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.wsgi.runwsgi = lambda func, addr = None: web.wsgi.runfcgi(func, addr)
    app.run()

#if __name__ =="__main__":
#    #app = web.application(urls, globals())
#    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
#    app.run()


