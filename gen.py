def gen2():
    yield range(10, 0, -1)


def gen1():
    yield gen2()


for j in gen1():
    for i in j:
        print(i)
