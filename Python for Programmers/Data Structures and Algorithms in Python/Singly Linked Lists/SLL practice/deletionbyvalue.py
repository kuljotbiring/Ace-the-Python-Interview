class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous Node does not exist")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    # delete a Node
    def delete_node(self, key):
        # deleting the head of the Linked List
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        # deleting Node other than head

        # keep track of prev Node of the Node to be deleted
        prev_node = None
        # while we have not found the key
        while curr_node and curr_node.data != key:
            # keep track of the prev Node while we update current Node
            prev_node = curr_node
            curr_node = curr_node.next

        # if we never found the key - simply return
        if curr_node is None:
            return

        # update prev node to the Node after the Node we are going to delete
        prev_node.next = curr_node.next
        curr_node = None
