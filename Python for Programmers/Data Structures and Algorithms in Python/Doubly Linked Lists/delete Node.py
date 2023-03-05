class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, key):
        curr = self.head
        while curr:
            if curr.data == key and curr == self.head:
                # deleting only Node present
                if not curr.next:
                    curr = None
                    self.head = None
                    return
                else:
                    # deleting head Node
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return
            elif curr.data == key:
                # delete Node other than head and not and end of LL
                if curr.next:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return
            else:
                # deleting last Node
                prev = curr.prev
                prev.next = None
                curr.prev = None
                curr = None
                return
            curr = curr.next


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.delete(1)
dllist.delete(6)
dllist.delete(4)

dllist.delete(3)
dllist.print_list()
