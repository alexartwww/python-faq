if __name__ == '__main__':
    # array
    list = []
    list.append(1)
    list.append(1)
    list.append(1)
    list.sort()
    len(list)

    # slices
    m = range(200)
    print('m[0:100:10]')
    a = m[0:100:10]
    print(a)
    print('m[::-1]')
    b = m[::-1]
    print(b)
    print('m[10:]')
    c = m[10:]
    print(c)
    print('m[:10]')
    d = m[:10]
    print(d)
    print('m[:-10]')
    e = m[:-10]
    print(e)
    print('m[-10:]')
    f = m[-10:]
    print(f)
    print('m[-20:-10]')
    g = m[-20:-10]
    print(g)

    # structure
    tuple = (1, 2, 3, )
    len(tuple)
    tuple.index(2)
    # array key => value
    # vs php array: doesn't remember order
    dict = {'a': 123, 'b': 234, 'c': 345}
    dict.keys()
    dict.values()
    set = set(['a','b','c']); # vs lists: unique, unordered, in works faster, only hashable objects
    frozenset = frozenset(['e','f','g']) # vs set: you can't change it
