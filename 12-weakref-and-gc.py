### http://asvetlov.blogspot.ru/2013/05/gc.html
### https://stackoverflow.com/questions/9908013/weak-references-in-python

import weakref
import gc

class MyObject(object):
    def my_method(self):
        print('my_method was called!')

obj = MyObject()
r = weakref.ref(obj)

gc.collect()
r().my_method()
assert r() is obj #r() allows you to access the object referenced: it's there.

obj = 1 #Let's change what obj references to
gc.collect()
assert r() is None #There is no object left: it was gc'ed.
