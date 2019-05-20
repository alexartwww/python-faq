def init(self, a=0):
    self.a = a


def view(self):
    print(self.a)


def set(self, a):
    self.a = a
    return self


def get(self):
    return self.a


A = type('A', (), {'__init__': init, 'view': view, 'set': set, 'get': get})

a = A(1)
a.set(2)
a.view()


class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print('-----------------------------------')
        print("Allocating memory for class", name)
        print(meta)
        print(bases)
        print(dct)
        print(dir(meta))
        def test_new(self):
            self.a += 2
            return self.a
        dct['test'] = test_new
        return super().__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('-----------------------------------')
        print("Initializing class", name)
        print(cls)
        print(bases)
        print(dct)
        print(dir(cls))
        super().__init__(name, bases, dct)

class MetaSigleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in MetaSigleton.instances:
            MetaSigleton.instances[cls] = super().__call__(*args, **kwargs)
        return MetaSigleton.instances[cls]

class B(object):
    pass

class MyClass(B, metaclass=MyMeta):
    def __new__(cls):
        print('-----------------------------------')
        print("Allocating memory for object")
        print(cls)
        print(dir(cls))
        return super().__new__(cls)

    def __init__(self, a=0):
        print('-----------------------------------')
        print("Initializing object")
        print(self)
        print(dir(self))
        self.a = a
        super().__init__()

    def test(self):
        self.a += 1
        return self.a


a = MyClass()
print(a.test())
print(a.test())
print(a.test())
b = MyClass()
print(b.test())
print(b.test())
print(b.test())
