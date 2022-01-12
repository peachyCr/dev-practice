class Queue(object):
    def __init__(self):
        self.lst = []

    def add_elem(self, elem):
        self.lst.append(elem)

    def pop(self):
        return self.lst.pop(0)


a = Queue()
a.add_elem("s")
a.add_elem("h")
a.add_elem("e")
a.add_elem("r")
print(a.pop())
