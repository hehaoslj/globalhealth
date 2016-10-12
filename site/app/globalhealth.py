#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import os
import sys
import metroui
import base_config
import markdown
import __builtin__

urls = (
'/reload/(.*)', 'update',
'/[^/]*', 'index',
'/([^/]*)/(.*)', 'trsite',

)

#app = web.application(urls, globals()) 

cur_path = os.path.dirname(os.path.abspath(__file__))
up_path = os.path.dirname(cur_path)

config_file = os.path.join(cur_path, 'conf.json')


class conf(base_config.Config):
    def __init__(self):
        self.web = web
        self.mui=metroui
        self.mui.conf = self
        self.lang = 'zh-CN'

    def tr(self, s):
        pos = 0
        try:
            pos = self.site.lang.index(self.lang)
            if hasattr(self, 'trans'):
                if self.trans.__dict__.has_key(s) :
                    return self.trans.__dict__[s][pos]
        except:
            pass

        return s

    def url(self, s=None, lang=None):
        if lang == None:
            lang = self.lang

        u = '/' + lang
        if s == None:
            s = web.ctx.fullpath
            sl = s.split('/')
            for i in range(len(sl), -1, -1):
                if sl[i-1] in self.site.lang:
                    sl.pop(i-1)
            return u+'/'.join(sl)

        return '/'.join((u, s))



render = web.template.render(up_path+'/template/' #Template folder
    , base='base' #Template base
    , globals=globals()
    , builtins=__builtin__.__dict__ )

ctx = conf()
#ctx.loadf(os.path.join(cur_path, 'conf.json'))
#ctx.lang = ctx.site.lang[0]
class update(object):
    def GET(self, cf='conf.json'):
        config_file = cf
        if cf == '':
            config_file = "conf.json"
        if config_file[-5:] != '.json':
            config_file += '.json'
        global ctx
        ctx = conf()
        ctx.loadf(config_file)
        ctx.lang = ctx.site.lang[0]
        return render.index()

class index(object):
    def GET(self, *args):
        return render.index()


class trsite(object):
    def GET(self, lang, url):
        ctx.lang = lang
        if ctx.lang not in ctx.site.lang:
            ctx.lang = ctx.site.lang[0]
        if url == '':
            return render.index()
        elif url == 'start':
            return render.start()
        else:
            return render.index()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        config_file = argv[1]

    app = web.application(urls, globals(), autoreload=True)
    web.wsgi.runwsgi = lambda func, addr = None: web.wsgi.runfcgi(func, addr)
    app.run()

#if __name__ =="__main__":
#    #app = web.application(urls, globals())
#    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
#    app.run()


