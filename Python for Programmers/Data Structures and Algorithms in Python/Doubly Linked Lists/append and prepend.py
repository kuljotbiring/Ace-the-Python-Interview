class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # if LL is empty, make new Node the head Node
        if self.head is None:
            self.head = Node(data)
        else:
            # make a new Node
            new_node = Node(data)
            curr = self.head
            # iterate through the LL
            while curr.next:
                curr = curr.next
            # make the next of curr the new Node
            curr.next = new_node
            # make the prev of new Node curr
            new_node.prev = curr

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            # make a new Node
            new_node = Node(data)
            # make old head prev be the new Node
            self.head.prev = new_node
            # make new Node next the old head
            new_node.next = self.head
            # make the new Node the head
            self.head = new_node

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next


dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.print_list()
