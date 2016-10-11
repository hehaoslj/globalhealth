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
    lang = 'en'
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
        if self.lang == 'en':
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
