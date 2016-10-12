#!/usr/bin/env python
#-*- coding: utf-8 -*-


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
        elif 'attrs' in self.attributes:
            self.attributes.update( self.attributes['attrs'] )
            del self.attributes['attrs']
        self.children = args

    def __str__(self):
        attr = ' '.join(['{}="{}"'.format(name, value) for name, value in self.attributes.items()])
        ctx = ''
        
        if type(self.children) in(str, unicode):
            ctx = str(self.children)
        else:# type(self.children) in (tuple, list):
            ctx = ''.join([str(child) for child in self.children])
        
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
    default_attributes={'cls':"app-bar fixed-top navy ", 'data-role':"appbar"}
    def __init__(self, config, obj):
        div.__init__(self)
        ctx = div(self.branding(config, obj), self.menu(config, obj), self.menutail(config, obj), cls="container")
        self.children=str(ctx)

    def options(self, config):
        class _O(object):
            pass
        o = _O()
        o.name="Options"
        o.href="#"
        o.menu=list()
        e=_O()
        e.name="en"
        e.href=config.url(lang="en")
        o.menu.append(e)
        e=_O()
        e.name="zh-CN"
        e.href=config.url(lang="zh-CN")
        o.menu.append(e)

        return '<li class="navbar-right">'+self.submenu(o, config=config)[4:]

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
            return u'<li><a href="{href}"> {name} </a></li>\n'.format(href=href, name=nm, order=order, order1=order+1)
        else:
            return u'''<li><a href="#" class="dropdown-toggle"> {name} </a>
<ul class="d-menu" data-role="dropdown" data-no-close="true" style="display: none;">
<li class="active"><a href="{href}">{name}</a></li>
<li class="divider"></li>

'''.format(href=href, name=nm, order=order, order1=order+1)+ '\n'.join([self.submenu(o,config=config, prefix=href) for o in obj.menu ])+ '</ul></li>\n'


    def menu(self, config, obj):
        self.order = 0
        s = u'''<ul class="app-bar-menu small-dropdown">'''+ '\n'.join([self.submenu(o, config=config, prefix='/'+config.lang) for o in zip(obj, range(len(obj)) ) ])+ self.options(config) + '</ul>\n'
        return s.encode('utf-8')

    def branding(self, config, obj):
        title = config.tr(config.site.start)
        s = u'\n<a href="{url}" class="app-bar-element branding"><img src="/static/favicon.ico" style="height: 28px; display: inline-block; margin-right: 10px;">{title}</a>\n\n'.format(title=title, url=config.url('start'))
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
