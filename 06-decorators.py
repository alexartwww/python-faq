def make_bold(fn):
    def wrapper(text):
        return "<b>" + fn(text) + "</b>"

    return wrapper

def make_italic(fn):
    def wrapper(text):
        return "<i>" + fn(text) + "</i>"

    return wrapper

@make_bold
@make_italic
def hello(text):
    return text

if __name__ == '__main__':
    print(hello('hello world'))
# ######################################################################################

def make_html(html):
    def decorator(fn):
        def wrapper(text):
            if html == 'bold':
                return "<b>" + fn(text) + "</b>"
            elif html == 'italic':
                return "<i>" + fn(text) + "</i>"
        return wrapper
    return decorator

@make_html('italic')
@make_html('bold')
def hi(text):
    return text

if __name__ == '__main__':
    print(hi('hi world'))
# ######################################################################################


def decorator(cls):
    class Wrapper(object):
        def __init__(self, *args, **kwargs):
            super().__setattr__('wrapped', cls(*args, **kwargs))
            # self.__dict__['wrapped'] = cls(*args, **kwargs)

        def __getattr__(self, name):
            print('Getting the {}'.format(name))
            return getattr(self.wrapped, name)

        def __setattr__(self, name, value):
            print('Setting the {} = {}'.format(name, value))
            return setattr(self.wrapped, name, value)

        def test(self, text):
            return '<b>' + self.wrapped.test2(text) + '</b>' + self.wrapped.ddd

    return Wrapper

@decorator
class C(object):
    def __init__(self):
        self.ddd = 'cool'


    def test(self, text):
        return text


    def test2(self, text):
        return text[::-1]


if __name__ == '__main__':
    x = C()
    print(x.test('hellow'))
    x.ddd = 'warm'
    print(x.test('hellow'))

# ######################################################################################

def decorator(html):
    def decorator(cls):
        class wrapper(object):
            def __init__(self, *args, **kwargs):
                super().__setattr__('wrapped', cls(*args, **kwargs))
                # self.__dict__['wrapped'] = cls(*args, **kwargs)

            def __call__(self, *args, **kwargs):
                print(1)

            def test(self, text):
                if html == 'bold':
                    return "<b>" + self.wrapped.test(text) + "</b>"
                elif html == 'italic':
                    return "<i>" + self.wrapped.test(text) + "</i>"

        return wrapper
    return decorator

@decorator('italic')
class C(object):
    def __init__(self):
        pass

    def test(self, text):
        return text


if __name__ == '__main__':
    x = C()
    x()
    print(x.test('hi'))



def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MySingleton2(object):
    y = 10

if __name__ == '__main__':
    x = MySingleton2()
    print(x.y)
    print(id(x))
    x.y = 20
    z = MySingleton2()
    print(id(z))
    print(z.y)

