class MyIterator(object):
    def __init__(self, maxNum):
        print('__init__', maxNum)
        self.maxNum = maxNum
        self.currentIndex = 0

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        if self.currentIndex >= self.maxNum:
            raise StopIteration
        nowIndex = self.currentIndex
        self.currentIndex += 1
        return nowIndex

    def __reversed__(self):
        print('__reversed__')
        if self.currentIndex < 0:
            raise StopIteration
        nowIndex = self.currentIndex
        self.currentIndex -= 1
        return nowIndex

if __name__ == '__main__':
    test_iter = MyIterator(10)
    for i in test_iter:
        print(i)
