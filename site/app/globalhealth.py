#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import os
import metroui
import base_config
import markdown
import __builtin__

urls = ( '/[^/]*', 'index',
'/([^/]*)/(.*)', 'trsite',

)

#app = web.application(urls, globals()) 

cur_path = os.path.dirname(os.path.abspath(__file__))
up_path = os.path.dirname(cur_path)



class conf(base_config.Config):
    def __init__(self):
        self.web = web
        self.mui=metroui
        self.mui.conf = self
        self.lang = 'zh-CN'

    def tr(self, s):
        pos = 0 #Chinese
        if self.lang == 'en':
            pos = 1

        if hasattr(self, 'trans'):
            if self.trans.__dict__.has_key(s) :
                return self.trans.__dict__[s][pos]

        return  s
    def url(self, s=None, lang=None):
        if lang == None:
            lang = self.lang

        u = '/zh-CN'
        if lang == 'en':
            u = '/en'

        if s == None:
            s = web.ctx.fullpath
            sl = s.split('/')
            for i in range(len(sl), -1, -1):
                if sl[i-1] in ('en', 'zh-CN'):
                    sl.pop(i-1)
            return u+'/'.join(sl)

        return '/'.join((u, s))



render = web.template.render(up_path+'/template/' #Template folder
    , base='base' #Template base
    , globals=globals()
    , builtins=__builtin__.__dict__ )

ctx = conf()
ctx.loadf(os.path.join(cur_path, 'conf.json'))

class index(object):
    def GET(self, *args):
        return render.index()


class trsite(object):
    def GET(self, lang, url):
        ctx.lang = lang
        if ctx.lang not in ('zh-CN', 'en'):
            ctx.lang = 'zh-CN'
        if url == '':
            return render.index()
        elif url == 'start':
            return render.start()
        else:
            return render.index()

if __name__ == "__main__":
    app = web.application(urls, globals(), autoreload=True)
    web.wsgi.runwsgi = lambda func, addr = None: web.wsgi.runfcgi(func, addr)
    app.run()

#if __name__ =="__main__":
#    #app = web.application(urls, globals())
#    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
#    app.run()


