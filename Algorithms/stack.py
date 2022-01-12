class Stack(object):
    def __init__(self):
        self.lst = []

    def add_elem(self, elem):
        self.lst.append(elem)

    def pop(self):
        last = self.lst.pop(-1)
        return last

a = Stack()
a.add_elem(5)
a.add_elem(9)
a.add_elem(90)


def kek(a, *args, b=None, **kwargs):
    print(args)
    print(kwargs)
    s1 = a + sum(args)
    s2 = b + sum(kwargs.values())
    return s1, s2

print(kek(1, 2, 3, 4 ,5 ,6, b=5, c=10, d=15, e=20))