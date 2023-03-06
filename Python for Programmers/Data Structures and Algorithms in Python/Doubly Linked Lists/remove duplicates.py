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

    def delete_node(self, key):
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

    def reverse(self):
        curr = self.head
        temp = None
        while curr:
            # save value of curr.prev in temp variable
            temp = curr.prev
            # swap values of curr.prev and curr.next
            curr.prev = curr.next
            curr.next = temp
            # move to next node
            curr = curr.prev

        if temp:
            self.head = temp.prev

    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.delete_node(1)
dllist.delete_node(6)
dllist.delete_node(4)

dllist.delete_node(3)
dllist.print_list()
