class Node:

    def __init__(self, data):
        # store data and next node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # points to first node in linked list
        self.head = None

    def append(self, data):
        # creating a new node
        new_node = Node(data)

        # if linked list is empty - point head to the newly created code
        if self.head is None:
            self.head = new_node
            return
