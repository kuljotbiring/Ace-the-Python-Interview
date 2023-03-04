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
        pass

    def print_list(self):
        pass