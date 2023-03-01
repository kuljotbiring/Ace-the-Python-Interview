class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        # if LL is empty
        if not self.head:
            # give the LL a circular effect
            new_node.next = new_node
        else:
            # move through list until we get to last Node
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        # if linked list is empty
        if not self.head:
            # make the Node and make it the head
            self.head = Node(data)
            # make the head point back to itself - circular
            self.head.next = self.head
        else:
            # make new node and start at head
            new_node = Node(data)
            curr = self.head
            # iterate through the list while not at last Node
            while curr.next != self.head:
                curr = curr.next
            # add new Node to the end
            curr.next = new_node
            # make new Node next point back to the head
            new_node.next = self.head

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break
