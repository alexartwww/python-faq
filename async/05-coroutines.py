def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received:', message)


def initgen(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


@initgen
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except BlaBlaException:
            print('.......................................')
            break
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average