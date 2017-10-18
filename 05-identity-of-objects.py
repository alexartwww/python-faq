'''
id()
'''

if __name__ == '__main__':
    a = 300000
    b = 300000
    print('a = {} b = {}'.format(a, b))
    print(id(a))
    print(id(b))
    print(a is b)
    print(a == b)

    a = {'a': 1, 'b': 3}
    b = {'a': 1, 'b': 3}
    print('a = {} b = {}'.format(a, b))
    print(id(a))
    print(id(b))
    print(a is b)
    print(a == b)
