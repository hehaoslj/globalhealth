#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random

color_templ="""black white lime green emerald teal blue cyan cobalt indigo violet pink magenta crimson red orange amber yellow brown olive steel mauve taupe gray dark darker darkBrown darkCrimson darkMagenta darkIndigo darkCyan darkCobalt darkTeal darkEmerald darkGreen darkOrange darkRed darkPink darkViolet darkBlue lightBlue lightRed lightGreen lighterBlue lightTeal lightOlive lightOrange lightPink grayDark grayDarker grayLight grayLighter"""

color_prefix_templ="bg fg ribbed"

colors = color_templ.split(" ")
color_prefixs = color_prefix_templ.split(' ')

random.seed(1)

def rand_color():
    pos = random.randint(0, len(colors)-1)
    px = random.randint(0, len(color_prefixs)-1)
    return '-'.join((color_prefixs[px], colors[pos]) )

class HTMLElement(object):
    default_attributes={}
    tag = "unknown_tag"
    nullable = False
    def __init__(self, *args, **kwargs):
        self.attributes = kwargs
        self.attributes.update(self.default_attributes)
        if 'cls' in self.attributes:
            self.attributes['class'] = self.attributes['cls']
            del self.attributes['cls']
        if 'attrs' in self.attributes:
            self.attributes.update( self.attributes['attrs'] )
            del self.attributes['attrs']
        if 'ctx' in self.attributes:
            self.children = self.attributes['ctx']
            del self.attributes['ctx']
        else:
            self.children = args

    def tostr(self, o):
        if o == None:
            return ''
        if type(o) == str:
            return o
        elif type(o) == unicode:
            return o.encode('utf-8')
        elif type(o) in (tuple, list):
            return ''.join([self.tostr(child) for child in o])
        else:
            return str(o)

    def __str__(self):
        attr = ' '.join(['{}="{}"'.format(name, value) for name, value in self.attributes.items()])
        ctx = ''
        ctx = self.tostr(self.children)
        #if type(self.children) ==str:
        #    ctx = self.children
        #elif type(self.children) == unicode:
        #    ctx = self.children.encode('utf-8')
        #elif type(self.children) in (tuple, list):
        #    ctx = ''.join([str(child) for child in self.children])

        if ctx == '' and self.nullable == True:
            return ''
            
        return '\n<{} {}>{}</{}>\n'.format(self.tag, attr, ctx, self.tag)
        
class div(HTMLElement):
    tag = "div"

class ndiv(div):
    nullable = True
    
class anchor(HTMLElement):
    tag = 'a'

class nanchor(anchor):
    nullable = True

class h1(HTMLElement):
    tag = 'h1'
class image(HTMLElement):
    tag='img'


class tile(div):
    default_attributes={'cls' : 'col-sm-6 col-md-3'}
    label = 'Tile'
    href='#'
    color='tile-red'
    def __init__(self, *args, **kwargs):
        div.__init__(self, **kwargs)
        
        if len(args) > 0:
            self.label = str(args[0])
        
        if len(args)>1:
            self.href=str(args[1])
        
        if len(args)>2:
            self.color = str(args[2])
        
        for k,v in kwargs.items():
            self.__setattr__(k, v)
        self.update()
    
    def __setattr__(self, key, value):
        if not self.__dict__.has_key(key):
            self.__dict__[key] = value
        else:
            self.__dict__[key] = value
        
        #print key, value
        self.update()
    def update(self):
        htitle = h1(self.label)
        ha = anchor(htitle, href=self.href)
        thumb = div(ha, cls='thumbnail tile tile-medium ' + self.color)
        self.__dict__['children'] = str( thumb )

class span(HTMLElement):
    tag = 'span'

class nspan(span):
    nullable = True

class button(HTMLElement):
    tag = 'button'


class topnav(HTMLElement):
    default_attributes={'cls':'navbar navbar-inverse navbar-fixed-top'}
    tag = 'nav'
    title = 'Project'
    toggle = 'Toggle Navigation'
    """<nav class="navbar navbar-inverse navbar-fixed-top">
     <div class="container">
       <div class="navbar-header">
         <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
           <span class="sr-only">$tr('Toggle navigation')</span>
           <span class="icon-bar"></span>
           <span class="icon-bar"></span>
           <span class="icon-bar"></span>
         </button>
         <a class="navbar-brand" href="#">$tr('Project name')</a>
       </div>
       <div id="navbar" class="navbar-collapse collapse">
         <form class="navbar-form navbar-right">
           <div class="form-group">
             <input type="text" placeholder="$tr('Email')" class="form-control">
           </div>
           <div class="form-group">
             <input type="password" placeholder="$tr('Password')" class="form-control">
           </div>
           <button type="submit" class="btn btn-success">Sign in</button>
         </form>
       </div><!--/.navbar-collapse -->
     </div>
   </nav>"""
    
    def __init__(self, *args, **kwargs):
        HTMLElement.__init__(self, **kwargs)
        
        if(len(args) > 1):
            self.title = args[0]
        if(len(args) >2):
            self.toggle = args[1]
        
        for k,v in kwargs.items():
            self.__setattr__(k, v)
        self.update()
    def update(self):
        eng = None
        chs = None
        if conf.lang == 'en':
            eng=anchor('English', cls='btn btn-default active', role='button', href='/en/')
            chs=anchor('Chinese', cls='btn btn-success', role='button', href='/zh-CN/')
        else:
            eng=anchor('English', cls='btn btn-success', href='/en/')
            chs=anchor('Chinese', cls='btn btn-default active', href='/zh-CN/')

        frm = div(chs, eng, cls="navbar-right")
        bar = div(frm, attrs={'id':"navbar", 'class':"navbar-collapse collapse"})
        
        sr = span(self.toggle, cls="sr-only")
        ic = span(cls="icon-bar")
        btn = button(sr, ic, ic, ic, attrs={'type':"button", 'class':"navbar-toggle collapsed", 'data-toggle':"collapse", 'data-target':"#navbar", 
        'aria-expanded':"false", 'aria-controls':"navbar"})
        a = anchor(self.title, cls="navbar-brand", href="#")
        hd = div(btn, a, cls="navbar-header")
        ctx = div(hd, bar, cls="container")
        self.__dict__['children'] = str(ctx)
    def __setattr__(self, key, value):
        if not self.__dict__.has_key(key):
            self.__dict__[key] = value
        else:
            self.__dict__[key] = value
        
        #print key, value
        self.update()

class menubar(div):
    """
    <header class="app-bar fixed-top navy" data-role="appbar">
        <div class="container">
            <a href="/" class="app-bar-element branding"><img src="images/wn8.png" style="height: 28px; display: inline-block; margin-right: 10px;"> Metro UI CSS</a>

            <ul class="app-bar-menu small-dropdown">
                <li data-flexorderorigin="0" data-flexorder="1" class="">
                    <a href="#" class="dropdown-toggle">Base CSS</a>
                    <ul class="d-menu" data-role="dropdown" data-no-close="true" style="display: none;">
                        <li class="disabled"><a href="overview.html">Overview</a></li>
                        <li class="divider"></li>
                        <li>
                            <a href="" class="dropdown-toggle">Grid system</a>
                            <ul class="d-menu" data-role="dropdown">
                                <li><a href="grid.html">Simple grid</a></li>
                                <li><a href="flexgrid.html">Flex grid</a></li>
                            </ul>
                        </li>
                        <li><a href="typography.html">Typography</a></li>
                        <li><a href="tables.html">Tables</a></li>
                        <li><a href="inputs.html">Forms &amp; Inputs</a></li>
                        <li><a href="buttons.html">Buttons</a></li>
                        <li><a href="images.html">Images</a></li>
                        <li><a href="font.html">Metro Icon Font</a></li>
                        <li class="divider"></li>
                        <li><a href="colors.html">Colors</a></li>
                        <li><a href="helpers.html">Helpers classes</a></li>
                        <li class="divider"></li>
                        <li><a href="rtl.html">RTL Support</a></li>
                        <li class="disabled"><a href="responsive.html">Responsive</a></li>
                    </ul>
                </li>
            </ul>

            <span class="app-bar-pull"></span>
            <div class="app-bar-pullbutton automatic" style="display: none;"></div>
            <div class="clearfix" style="width: 0;"></div>
            <nav class="app-bar-pullmenu hidden flexstyle-app-bar-menu" style="display: none;">
                <ul class="app-bar-pullmenubar hidden app-bar-menu"></ul>
            </nav>
    </div>
    </header>
    """
    tag = 'header'
    default_attributes={'cls':"app-bar fixed-top navy no-flexible", 'data-role':"appbar"}
    def __init__(self, config, obj):
        div.__init__(self)
        ctx = div(self.branding(config, obj), self.menu(config, obj), self.menutail(config, obj), cls="container")
        self.children=str(ctx)

    def options(self, config):
        class _O(object):
            pass
        o = _O()
        o.name="Options"
        o.href="options"
        o.menu=list()
        e=_O()
        e.name="en"
        e.href=config.url(lang="en")
        o.menu.append(e)
        e=_O()
        e.name="zh-CN"
        e.href=config.url(lang="zh-CN")
        o.menu.append(e)

        rt='<li class="navbar-right">'+self.submenu(o, config=config)[4:]
        return rt

    def submenu(self, o, config, prefix=""):
        obj = o
        order = 0
        if type(o) == tuple:
            obj, order = o

        if obj.name=='--':
            return '<li class="divider"></li>\n'

        nm = config.tr(obj.name)
        href = obj.href
        if href[0] != '/':
            href = '/'.join((prefix, obj.href))
        if obj.href == "#":
            href = "#"
            prefix = ""

        if hasattr(obj, "menu") == False:
            rt = u'<li><a href="{href}"> {name} </a></li>\n'.format(href=href, name=nm, order=order, order1=order+1)
            return rt
        else:
            rt=u'''<li><a href="#" class="dropdown-toggle"> {name} </a>
<ul class="d-menu" data-role="dropdown" data-no-close="true" style="display: none;">
<li class="active"><a href="{href}">{name}</a></li>
<li class="divider"></li>

'''.format(href=href, name=nm, order=order, order1=order+1)+ '\n'.join([self.submenu(o,config=config, prefix=href) for o in obj.menu ])+ '</ul></li>\n'
            return rt


    def menu(self, config, obj):
        self.order = 0
        s = u'''<ul class="app-bar-menu small-dropdown">'''+ '\n'.join([self.submenu(o, config=config, prefix='/'+config.lang) for o in zip(obj, range(len(obj)) ) ])+ self.options(config) + '</ul>\n'
        return s.encode('utf-8')

    def branding(self, config, obj):
        title = config.tr(config.site.start)
        s = u'\n<a href="{url}" class="app-bar-element branding"><i class="icon icon-windows icon-2x"></i></a>\n\n'.format(title=title, url=config.url('start'))
        return s.encode('utf-8')

    def menutail(self, c, o):
        return """
<span class="app-bar-pull"></span>
    <div class="app-bar-pullbutton automatic" style="display: none;"></div>
    <div class="clearfix" style="width: 0;"></div>
    <nav class="app-bar-pullmenu hidden flexstyle-app-bar-menu" style="display: none;">
        <ul class="app-bar-pullmenubar hidden app-bar-menu"></ul>
</nav>
        """

def parse_cls(fn, *args, **kw):
    def wrapped(*args, **kw):
        bg = kw['bg'] if kw.has_key('bg') else rand_color()
        fg = kw['fg'] if kw.has_key('fg') else "fg-white"
        cls = kw['cls'] if kw.has_key('cls') else 'tile'
        url = kw['url'] if kw.has_key('url') else None
        cls=' '.join((bg, fg, cls))

        lcls = "tile-label"
        if kw.has_key('label_cls'):
            lcls += ' ' + kw['label_cls']
        s1=nspan(kw['text'], cls=lcls)

        if url:
            o=anchor(fn(*args, tile_label=s1, **kw), href=url, cls=cls, attrs={'data-role':"tile"})
            return o
        else:
            o = div(fn(*args, tile_label=s1, **kw), cls=cls, attrs={'data-role':"tile"})
            return o
    return wrapped

@parse_cls
def tile1(icon="", **kw):
    """<!-- Tile with icon, icon can be font icon or image -->"""
    ctx=[kw['tile_label']]
    s = span(cls="icon %s" % icon)
    ctx.append(s)

    d2 = div(ctx=ctx, cls="tile-content iconic")
    return d2

@parse_cls
def tile_image(img="", **kw):
    ctx=[kw['tile_label']]
    s=image(src=img)
    ctx.append(s)

    if kw['text']:
        s=nspan(kw['text'], cls="tile-label")
        ctx.append(s)
    d2 = div(ctx=ctx, cls="tile-content")
    return d2

@parse_cls
def tile2(label="",badge="", **kw):
    """<!-- Tile with label and badge -->
    <div class="tile">
        <div class="tile-content ">
            <span class="tile-label">Label</span>
            <span class="tile-badge">5</span>
        </div>
    </div>"""
    ctx=[kw['tile_label']]
    s1=nspan(kw['text'], cls="tile-label")
    s2 = span(badge, cls="tile-badge")
    ctx.append(s1)
    ctx.append(s2)
    d2=None
    if kw.has_key('icon'):
        s3 = span(cls="icon %s" % kw['icon'])
        ctx.append(s3)
        d2 = div(ctx=ctx, cls="tile-content iconic")
    elif kw.has_key('image'):
        s3 = image(src=kw['image'])
        ctx.append(s3)
        d2 = div(ctx=ctx, cls="tile-content iconic")
    else:
        d2 = div(ctx=ctx, cls="tile-content")
    return d2

@parse_cls
def tile3(imgset=[], **kw):
    """<!-- Tile with image set (max 5 images) -->
    <div class="tile">
        <div class="tile-content image-set">
            <img src="...">
            <img src="...">
            <img src="...">
            <img src="...">
            <img src="...">
        </div>
    </div>"""
    ctx=[]
    ims = ""
    for img in imgset:
        i = image(src=img)
        ctx.append(i)
    ctx.append(kw['tile_label'])
    d2 = div(ctx=ctx, cls="tile-content image-set")
    return d2

@parse_cls
def tile4(imgctn="", overlay="", **kw):
    """<!-- Tile with image container -->
    <div class="tile">
        <div class="tile-content">
            <div class="image-container">
                <div class="frame">
                    <img src="...">
                </div>
                <div class="image-overlay">
                    Overlay text
                </div>
            </div>
        </div>
    </div>"""
    i=image(src=imgctn)
    d1 = div(i, cls="frame")
    d2 = div(overlay, cls="image-overlay")
    dic = div(d1, d2,kw['tile_label'], cls="image-container")
    dtc = div(dic, cls="tile-content")
    return dtc

@parse_cls
def tile_carousel(carousel=[], **kw):
    """<!-- Tile with carousel -->
    <div class="tile">
        <div class="tile-content">
            <div class="carousel" data-role="carousel">
                <div class="slide"><img src="..."></div>
                ...
                <div class="slide"><img src="..."></div>
            </div>
        </div>
    </div>"""
    ctx=[]
    for k in carousel:
        img=image(src=k, attrs={'data-role':"fitImage", 'data-format':"fill"})
        d1 = div(img, cls="slide")
        ctx.append(d1)
    ctx.append(kw['tile_label'])
    d2 = div(ctx=ctx, cls="carousel", attrs={'data-role':"carousel", 'data-controls':"false",'data-height':"100%", 'data-width':"100%"})
    dtc = div(d2, cls="tile-content")
    return dtc

@parse_cls
def tile_slide(slide="", over="", direction='slide-up', **kw):
    """<!-- Tile with slide-up effect -->
    <div class="tile">
        <div class="tile-content slide-up">
            <div class="slide">
                ... Main slide content ...
            </div>
            <div class="slide-over">
                ... Over slide content here ...
            </div>
        </div>
    </div>"""
    img = image(src=slide)
    s = div(img, cls="slide")
    o = div(over, cls="slide-over")
    dtc = div(s, o,kw['tile_label'], cls="tile-content %s" % direction)
    return dtc

@parse_cls
def tile_panel(panel="", header="", **kw):
    """<div class="tile-big tile-wide-y bg-white" data-role="tile">
    <div class="tile-content">
        <div class="panel" style="height: 100%">
            <div class="heading bg-darkRed fg-white"><span class="title text-light">Meeting</span></div>
            <div class="content fg-dark clear-float" style="height: 100%">
                ...
            </div>
        </div>
    </div>
</div>"""
    ctx = div(panel, cls="content fg-dark clear-float", style="height: 100%")
    s = kw['tile_label']
    hdr = div(s, cls="heading bg-darkOrange fg-white")
    pnl = div(hdr, ctx, cls="panel", style="height: 100%")
    dtc = div(pnl, cls="tile-content")
    return dtc



def Tile(*args, **kw):


    if kw.has_key('imgset'):
        return tile3(*args, **kw)
    elif kw.has_key('imgctn'):
        return tile4(*args, **kw)
    elif kw.has_key('carousel'):
        return tile_carousel(*args, **kw)
    elif kw.has_key('slide'):
        return tile_slide(*args, **kw)
    elif kw.has_key('img'):
        return tile_image(*args, **kw)
    elif kw.has_key('panel'):
        return tile_panel(*args, **kw)
    elif kw.has_key('label'):
        return tile2(*args, **kw)
    elif kw.has_key('icon'):
        return tile1(*args, **kw)
