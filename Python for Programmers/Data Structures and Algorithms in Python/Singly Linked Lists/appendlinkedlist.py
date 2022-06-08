class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # append adds a node to the end of a linked list
    def append(self, data):
        new_node = Node(data)
        # address case if linked list is empty
        if self.head is None:
            self.head = new_node
            return
        # if list is not empty
        last_node = self.head
        # while there are other nodes - keep moving through linked list
        while last_node.next:
            last_node = last_node.next
        # finally, make the last node point to the new node
        last_node.next = new_node
