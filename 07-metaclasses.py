'''
Metaclasses - the way to control class object
'''

# Class creation
class C(object):
    def __init__(self):
        self.a = 1

    def setA(self, param):
        self.a = param
if __name__ == '__main__':
    v = C()
    print(v.a) # 1
    v.setA(2)
    print(v.a) # 2

### OR ###

def setA(self, param):
    self.a = param

C = type('C', (), {'a': 1, 'setA': setA})
if __name__ == '__main__':
    v = C()
    print(v.a) # 1
    v.setA(2)
    print(v.a) # 2


class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print('-----------------------------------')
        print("Allocating memory for class", name)
        print(meta)
        print(bases)
        print(dct)
        print(dir(meta))
        return super().__new__(meta, name, bases, dct)

    def __call__(meta, *args, **kwds):
        print('-----------------------------------')
        print('__call__ of ', str(meta))
        print('__call__ *args=', str(args))
        return type.__call__(meta, *args, **kwds)

    def __init__(cls, name, bases, dct):
        print('-----------------------------------')
        print("Initializing class", name)
        print(cls)
        print(bases)
        print(dct)
        print(dir(cls))
        super().__init__(name, bases, dct)

class MyClass(object, metaclass=MyMeta):
    def __new__(cls):
        print('-----------------------------------')
        print("Allocating memory for object")
        print(cls)
        print(dir(cls))
        return super().__new__(cls)

    def __call__(cls, *args, **kwds):
        print('-----------------------------------')
        print('__call__ of ', str(cls))
        print('__call__ *args=', str(args))
        return type.__call__(cls, *args, **kwds)

    def __init__(self):
        print('-----------------------------------')
        print("Initializing object")
        print(self)
        print(dir(self))
        super().__init__()

if __name__ == '__main__':
    a = MyClass()
    a()

'''
-----------------------------------
Allocating memory for class MyClass
<class '__main__.MyMeta'>
(<class 'object'>,)
{'__qualname__': 'MyClass', '__new__': <function MyClass.__new__ at 0x7fed1be76e18>, '__module__': '__main__',
'__call__': <function MyClass.__call__ at 0x7fed1be76ea0>, '__init__': <function MyClass.__init__ at 0x7fed1be76f28>}
['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__',
'__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__',
'__hash__', '__init__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__',
'__ne__', '__new__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__',
'__weakrefoffset__', 'mro']
-----------------------------------
Initializing class MyClass
<class '__main__.MyClass'>
(<class 'object'>,)
{'__qualname__': 'MyClass', '__new__': <function MyClass.__new__ at 0x7fed1be76e18>, '__module__': '__main__',
'__call__': <function MyClass.__call__ at 0x7fed1be76ea0>, '__init__': <function MyClass.__init__ at 0x7fed1be76f28>}
['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
-----------------------------------
__call__ of  <class '__main__.MyClass'>
__call__ *args= ()
-----------------------------------
Allocating memory for object
<class '__main__.MyClass'>
['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
-----------------------------------
Initializing object
<__main__.MyClass object at 0x7fed1bddc940>
['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
-----------------------------------
__call__ of  <__main__.MyClass object at 0x7fed1bddc940>
__call__ *args= ()
'''



class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MySingleton2(object, metaclass=Singleton):
    y = 10

if __name__ == '__main__':
    x = MySingleton2()
    print(x.y)
    print(id(x))
    x.y = 20
    z = MySingleton2()
    print(id(z))
    print(z.y)
