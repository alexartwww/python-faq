if __name__ == '__main__':
    # array
    list = []
    list.append(1)
    list.append(1)
    list.append(1)
    list.sort()
    list.count()

    # slices
    a = m[0:100:10]
    b = m[1:10, 3:20]
    c = m[0:100:10, 50:75:5]
    m[0:5, 5:10] = n
    del m[:10, 15:]
    m[::-1]



    # structure
    tuple = (1, 2, 3, )
    tuple.count()
    tuple.index(2)
    # array key => value
    # vs php array: doesn't remember order
    dict = {'a': 123, 'b': 234, 'c': 345}
    dict.keys()
    dict.values()
    set = set(['a','b','c']); # vs lists: unique, unordered, in works faster, only hashable objects
    frozenset = frozenset(['e','f','g']) # vs set: you can't change it
