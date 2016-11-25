#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import datetime
import os
import sys
import metroui
import base_config
import markdown
import __builtin__

urls = (
'/([^/]*)/research(.*)', 'research',
'/([^/]*)/aboutus','aboutus',
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
        self.lang = 'en'

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
        if s[:4] == "http":
            return s
        return '/'.join((u, s))



render = web.template.render(up_path+'/template/' #Template folder
    , base='base' #Template base
    , globals=globals()
    , builtins=__builtin__.__dict__ )

ctx = conf()
#ctx.loadf(os.path.join(cur_path, 'conf.json'))
#ctx.lang = ctx.site.lang[0]

def reload_config(fn, *args, **kw):
    def wrapped(*args, **kw):
        config_file='conf.json'
        if kw.has_key('cf'):
            config_file = kw['cf']
        if config_file == '':
            config_file = "conf.json"
        if config_file[-5:] != '.json':
            config_file += '.json'
        global ctx
        ctx = conf()
        ctx.loadf(config_file)
        ctx.lang = ctx.site.lang[1]
        return fn(*args, **kw)
    return wrapped

def parse_lang(fn, *args, **kw):
    def wrapped(*args, **kw):
        if args[1] in ctx.site.lang:
            ctx.lang = args[1]
        else:
            ctx.lang = ctx.site.lang[0]
        return fn(*args, **kw)
    return wrapped

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
    @reload_config
    def GET(self, *args):
        return render.index()


class trsite(object):
    @reload_config
    def GET(self, lang, url):
        ctx.lang = lang
        if ctx.lang not in ctx.site.lang:
            ctx.lang = ctx.site.lang[1]

        if url == '':
            return render.index()
        elif url == 'start':
            return render.start()
        elif url[:3] == 'pi/':
            name = os.path.join(up_path,  "static", url)
            if ctx.lang != ctx.site.lang[0]:
                sl = url.split('/')[-1]
                url = url.replace(sl, ctx.lang+'_'+sl)
                n1 = os.path.join(up_path,  "static", url)
                name = n1 if os.path.exists(n1) else name

            f=open(name, 'r')
            s=f.read()
            f.close()
            return render.content(content=s, ctxtitle=ctx.tr("Principal Investigator"))

        elif url[:8] == 'meeting/':
            name = os.path.join(up_path,  "static", url)
            if ctx.lang == 'en':
                sl = url.split('/')[-1]
                url = url.replace(sl, 'en_'+sl)
                name = os.path.join(up_path,  "static", url)
            f=open(name, 'r')
            s=f.read()
            f.close()
            return render.content(content=s, ctxtitle=ctx.tr("Meeting"))
        elif url[:7] == 'meeting':
            u = '20161104.md'
            if ctx.lang == 'en':
                u = 'en_20161104.md'
            name = os.path.join(up_path, 'static', 'meeting', u)
            f=open(name, 'r')
            s=f.read()
            f.close()
            return render.content(content=s, ctxtitle=ctx.tr("Meeting"))
        else:
            return render.index()

class research(object):

    @reload_config
    @parse_lang
    def GET(self, lang, url):
        if url == '' or url=='/':
            return render.tile(tiles=['Research',])
        t=url.split('/')
        if len(t) ==2:
            return render.tile(tiles=[t[-1],])
        else:
            return url

class aboutus(object):
    @reload_config
    @parse_lang
    def GET(self, lang):
        name = os.path.join(up_path,  "static", "aboutus", "aboutus.md")
        if ctx.lang == 'en':
            name = os.path.join(up_path,  "static", "aboutus", "en_aboutus.md")
        if os.path.exists(name):
            f = open(name, 'r')
            s=f.read()
            f.close()
            return render.content(content=s, ctxtitle=ctx.tr("About us"))

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


