
def decoratorfunc_params(coefficient):
    if callable(coefficient):
        c = 2
        def wrapped(*args, **kwargs):
            return coefficient(*args) * c
        return wrapped
    else:
        def decoratorfunc(func):
            def wrapped(*args, **kwargs):
                return func(*args) * coefficient
            return wrapped
    return decoratorfunc


@decoratorfunc_params
def decoredfunc(*args):
    return sum(args)


print(decoredfunc(1, 2, 3))


def decoratorclass(klass):
    print(klass.__name__)
    print(list(klass.__bases__))
    print(list(klass.__dict__))
    return klass


class B(object):
    pass


@decoratorclass
class decoredclass(B):
    def __init__(self):
        self.a = 1

    def update_a(self, c):
        self.a += c

    def view_a(self):
        print(self.a)

obj = decoredclass()
obj.update_a(1)
obj.view_a()
