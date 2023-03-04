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

    def add_after_node(self, key, data):
        curr = self.head
        # run until curr is None
        while curr:
            # if we are inserting after last Node - call append function
            if curr.next is None and curr.data == key:
                self.append(data)
                return
            # inserting other than after last Node
            elif curr.data == key:
                new_node = Node(data)
                # store the next Node in a temp variable
                nxt = curr.next
                curr.next = new_node
                new_node.next = nxt
                new_node.prev = curr
                nxt.prev = new_node
                return
            # move through the LL
            curr = curr.next
