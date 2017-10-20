# http://www.diveintopython3.net/special-method-names.html

# Basic

class MyBasic(object):
    a = None
    b = None
    c = None

    def __new__(cls, *args, **kwargs):
        print('__new__')
        obj = super().__new__(cls)
        return obj

    def __init__(self, *args, **kwargs):
        print('__init__')
        print(kwargs)
        self.a = kwargs['a']
        self.b = kwargs['b']
        self.c = kwargs['c']

    def __call__(self, *args, **kwargs):
        print('__call__')
        return self

    def __repr__(self):
        print('__repr__')
        return '__repr__ MyBasic(a=%s, b=%s, c=%s)' % (self.a, self.b, self.c)

    def __str__(self):
        print('__str__')
        return '__str__ MyBasic(a=%s, b=%s, c=%s)' % (self.a, self.b, self.c)

    def __bytes__(self):
        print('__bytes__')
        return b'__bytes__ MyBasic'

    def __format__(self, format_spec):
        print('__format__', format_spec)
        return '__format__ MyBasic(a=%s, b=%s, c=%s)' % (self.a, self.b, self.c)

    def __del__(self):
        print('__del__')

    def __hash__(self):
        print('__hash__')
        return hash('__format__ MyBasic(a=%s, b=%s, c=%s)' % (self.a, self.b, self.c))

if __name__ == '__main__':
    a = MyBasic(a = 1, b = 2, c = 3)
    a()
    print(a)
    print(str(a))
    print(bytes(a))
    print('{}'.format(a))
    print(hash(a))

    del a

    '''
__new__
__init__
{'b': 2, 'c': 3, 'a': 1}
__call__
__str__
__str__ MyBasic(a=1, b=2, c=3)
__str__
__str__ MyBasic(a=1, b=2, c=3)
__bytes__
b'__bytes__ MyBasic'
__format__
__format__ MyBasic(a=1, b=2, c=3)
__hash__
4700799735243815556
__del__
'''

# Iterator

class MyIterator(object):
    def __init__(self, maxNum):
        print('__init__', maxNum)
        self.maxNum = maxNum
        self.currentIndex = 0

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        if self.currentIndex >= self.maxNum:
            raise StopIteration
        nowIndex = self.currentIndex
        self.currentIndex += 1
        return nowIndex

    def __reversed__(self):
        print('__reversed__')
        if self.currentIndex < 0:
            raise StopIteration
        nowIndex = self.currentIndex
        self.currentIndex -= 1
        return nowIndex

if __name__ == '__main__':
    test_iter = MyIterator(10)
    for i in test_iter:
        print(i)
'''
__init__ 10
__iter__
__next__
0
__next__
1
__next__
2
__next__
3
__next__
4
__next__
5
__next__
6
__next__
7
__next__
8
__next__
9
__next__
'''


# Iterator

class MyAttrs(object):
    myAttrs = {}
    def __init__(self):
        print('__init__')
        MyAttrs.myAttrs[id(self)] = {}
        self.a = 1


    '''def __getattribute__(self, name):
        print('__getattribute__', name)
        if name in MyAttrs.myAttrs[id(self)]:
            return MyAttrs.myAttrs[id(self)][name]
        else:
            return None'''

    def __getattr__(self, name):
        print('__getattr__', name)
        if name in MyAttrs.myAttrs[id(self)]:
            return MyAttrs.myAttrs[id(self)][name]
        else:
            return None

    def __setattr__(self, name, value):
        print('__setattr__', name, value)
        MyAttrs.myAttrs[id(self)][name] = value

    def __delattr__(self, name):
        print('__delattr__', name)
        if name in MyAttrs.myAttrs[id(self)]:
            del MyAttrs.myAttrs[id(self)][name]

if __name__ == '__main__':
    test_attrs = MyAttrs()
    test_attrs.a = 1
    print(test_attrs.a)
    print(test_attrs.b)
    del test_attrs.a

'''
__init__
__setattr__ a 1
__setattr__ a 1
__getattr__ a
1
__getattr__ b
None
__delattr__ a
'''

class MySet(object):
    def __init__(self):
        print('__init__')
        self.my_set = []

    def __len__(self):
        print('__len__')
        return len(self.my_set)

    def __contains__(self, item):
        print('__contains__')
        return item in self.my_set

class MyDict(object):
    def __init__(self):
        print('__init__')
        self.my_dict = {}

    def __getitem__(self, key):
        print('__getitem__')
        if key in self.my_dict:
            return self.my_dict[key]
        else:
            return None

    def __setitem__(self, key, value):
        print('__setitem__')
        self.my_dict[key] = value

    def __delitem__(self, key):
        print('__delitem__')
        if key in self.my_dict:
            del self.my_dict[key]

class MyNumber(object):
    def __init__(self, x, y):
        print('__init__')
        self.x = x
        self.y = y

    def __add__(self, other):
        print('__add__')
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        print('__sub__')
        self.x -= other.x
        self.y -= other.y
        return self

    def __radd__(self, other):
        print('__radd__')
        other.x += self.x
        other.y += self.y
        return other

    def __rsub__(self, other):
        print('__rsub__')
        other.x -= self.x
        other.y -= self.y
        return other

    def __neg__(self):
        print('__neg__')
        self.x = -self.x
        self.y = -self.y
        return self

    def __pos__(self):
        print('__pos__')
        self.x = self.x
        self.y = self.y
        return self

    def __eq__(self, other):
        print('__eq__')
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        print('__ne__')
        return self.x != other.x or self.y != other.y



if __name__ == '__main__':
    a = MyNumber(1,2)
    b = MyNumber(3,4)
    c = a + b
    d = b + a
    e = a - b
    d = b - a
    +a
    -a
    a == b
    a != b
