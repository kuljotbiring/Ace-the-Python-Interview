class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def iterative_reverse(self):
        curr = self.head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def recursive_reverse(self):
        def _recursive_reverse(curr, prev):
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return _recursive_reverse(curr, prev)
        self.head = _recursive_reverse(curr=self.head, prev=None)

    def merge_sorted(self, llist):
        dummy = Node(0)
        tail = dummy
        p = self.head
        q = llist.head

        while p and q:
            if p.data <= q.data:
                tail.next = p
                p = p.next
            else:
                tail.next = q
                q = q.next
            tail = tail.next

        if p:
            tail.next = p
        elif q:
            tail.next = q

        return dummy.next

    def count_occurrences(self, val):
        curr = self.head
        count = 0

        while curr:
            if curr.data == val:
                count += 1
            curr = curr.next

        return count


llist_2 = LinkedList()
llist_2.append(1)
llist_2.append(2)
llist_2.append(1)
llist_2.append(3)
llist_2.append(1)
llist_2.append(4)
llist_2.append(1)
print(llist_2.count_occurrences(1))
