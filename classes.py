class A(object):
    def __init__(self):
        self.a = 1

class B(object):
    def __init__(self):
        self.a = 2


class C(A, B):
    def __init__(self):
        self.a = 3
        super().__init__()

obj = C()
print(obj.a)
