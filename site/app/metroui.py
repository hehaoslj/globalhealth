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
            
        return '<{} {}>{}</{}>'.format(self.tag, attr, ctx, self.tag)
        
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
        div.__init__(self)
        
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
                        