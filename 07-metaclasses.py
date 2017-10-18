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
