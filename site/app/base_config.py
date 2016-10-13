#!/usr/bin/env python
# -*- coding: utf-8 -*-



import json
import inspect

class ConfigObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            return self.default(d)
        return obj

def config_object_hook(obj):
    c = Config(obj)
    print type(obj), 'hook', str(obj)
    return c



def config_dumps(obj):
    return json.dumps(obj, cls = ConfigObjectEncoder, indent = 4, sort_keys = True)



class Config(object):
    def dumpf(self, s):
        f=open(s, 'w')
        f.write(self.dumps())
        f.close()
    def dumps(self):
        return config_dumps(self, check_circular=False)
    def loads(self, s, cleanup=False):
        #print 'call loads'
        c = config_loads(s)
        if cleanup == True:
            self = c
        else:
            self.__dict__.update(c.__dict__)
    def dict(self):
        return json.loads( self.dumps() )
    def loadf(self, s, cleanup=False):
        f=open(s, 'r')
        ss = f.read()
        f.close()
        self.loads(ss, cleanup)

def dict_to_Config(d):
    c=Config()
    for k,v in d.items():
        c.__dict__[k] = v
    return c

def config_loads(s):
    return json.loads(s, object_hook=dict_to_Config)

def test():
    ctx=Config()
    ctx.c='qwqwq'
    ctx.loadf('conf.json')
    ctx.dumps()
    return ctx
