class Node:

    def __init__(self, data):
        # store data and next node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # points to first node in linked list
        self.head = None

    def print_list(self):
        # start at the head of list
        current_node = self.head

        # while we are not pointed at None
        while current_node:
            # print the data in the current Node
            print(current_node.data)
            # move the pointer over to iterate through list
            current_node = current_node.next

    def append(self, data):
        # creating a new node
        new_node = Node(data)

        # if linked list is empty - point head to the newly created code
        if self.head is None:
            self.head = new_node
            return
        # if the linked list is not empty
        # we define last node and START at the head
        # it will eventually point to the last node
        last_node = self.head
        # move from node to node until we get to none
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


sll = LinkedList()

sll.append("A")
sll.append("B")
sll.append("C")
