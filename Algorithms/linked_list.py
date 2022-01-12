class Node:
    def __init__(self, val):
        self.val = val
        self.next_val = None

    def __repr__(self):
        return str(self.val)


class SingleList(object):
    def __init__(self, value):
        self.head = Node(value)

    def push_back(self, value):
        tail = self.head
        while tail.next_val:
            tail = tail.next_val
        tail.next_val = Node(value)

    def delete(self):
        tail = self.head
        pre_tail = self.head
        while tail.next_val:
            pre_tail = tail
            tail = tail.next_val
        pre_tail.next_val = None

    def find_elem(self, index):
        elem = self.head
        i = 0
        while elem.next_val:
            if i == index:
                return elem.value
            elem = elem.next_val
            i += 1
        return None


a = SingleList(5)
