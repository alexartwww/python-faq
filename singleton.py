'''
def __new__(cls, ...) — статический метод (но его можно таковым не объявлять), который создает объект класса cls.

def __init__(self, ...) — метод класса, который инициализирует созданный объект.
'''

class MySingleton(object):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls.y = 10
        return cls._instance

    def test(self):
        print(123)


if __name__ == '__main__':
    x = MySingleton()
    print(x.y)
    print(x)
    x.test()
    x.y = 20
    z = MySingleton()
    print(z.y)
    print(z)
    z.test()



