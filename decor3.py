

def decor1(func):
    def wrapped(text):
        print('decor1')
        return "decor1( {} )".format(func(text))
    return wrapped

def decor2(func):
    def wrapped(text):
        print('decor2')
        return "decor2( {} )".format(func(text))
    return wrapped

def decor3(func):
    def wrapped(text):
        print('decor3')
        return "decor3( {} )".format(func(text))
    return wrapped



@decor3
@decor2
@decor1
def func(text):
    print('func')
    return text

if __name__ == '__main__':
    print(func('test'))
