def fun(addition):
    def decorator(wrapped):
        def other(a, b, c):
            return addition - a - b - c, wrapped(a, b, c)

        return other

    return decorator


@fun(22)
def some(a, b, c):
    return a + b + c


def decor(addition):
    def decorator(Wrapped):
        class Decorated(object):
            def __init__(self, a=0):
                self.a_obj = Wrapped(a + addition)

            def get(self):
                return self.a_obj.get()

            def set(self, a):
                return self.a_obj.set(a + addition)

            def view(self):
                self.a_obj.view()

        return Decorated

    return decorator


@decor(12)
class A(object):

    def __init__(self, a=0):
        self.set(a)

    def get(self):
        return self.a

    def set(self, a):
        self.a = a
        return self

    def view(self):
        print(self.a)


def singleton(Wrapped):
    instances = {}
    def get_instance(*args, **kwargs):
        if Wrapped not in instances:
            instances[Wrapped] = Wrapped(*args, **kwargs)
        return instances[Wrapped]
    return get_instance


def decor(pow_value):
    if callable(pow_value):
        def func(*args, **kwargs):
            return pow_value(*args, **kwargs) ** 2

        return func
    else:
        def powdecor(wrapped):
            def func(*args, **kwargs):
                return wrapped(*args, **kwargs) ** pow_value

            return func

        return powdecor


@decor(3)
def abc(a, b):
    return a + b


abc = decor(3)(abc)


@decor
def abc_2(a, b, c):
    return a + b + c


abc_2 = decor(abc_2)

if __name__ == '__main__':
    a = A(1)
    a.view()
    print(some(a=1, b=2, c=3))
