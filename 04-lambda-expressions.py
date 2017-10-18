'''
lambda - is small inline anonymous functions
'''

if __name__ == '__main__':
    a = lambda x, y: x + y
    print(a(1,2))
    b = lambda **kwargs: [(key, value) for key, value in kwargs.items() if key == 'a']
    print(b(a = 1, b = 2)) # [('a', 1)]
    # you can't do this(
    # b = lambda **kwargs: [(key, value) for key, value in kwargs.items() if key == 'a' else ('unknown', 'unknown')]
    b = 2
    c = 1 if b > 10 else 2
    print(c)
