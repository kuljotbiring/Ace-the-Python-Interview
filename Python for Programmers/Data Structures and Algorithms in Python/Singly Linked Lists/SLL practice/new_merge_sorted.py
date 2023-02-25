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

    def merge_sorted(self, llist):
        # create a dummy Node for edge case of inserting in empty LL
        tail = Node(0)
        # get the heads of each LL
        l1 = self.head
        l2 = llist.head

        # iterate through the list while both LL are not empty
        while l1 and l2:
            # if the value in List 1 less than or equal to value in List 2
            if l1.data <= l2.data:
                # make the next Node be the lower value Node
                tail.next = l1
                # move forward in the first List
                l1 = l1.next
            # value in List 2 is lower
            else:
                # make the next Node be the lower value Node
                tail.next = l2
                # move forward in the first List
                l2 = l2.next
            # now update the tail pointer
            tail = tail.next

        # if one list is empty and other is not
        # append that list to the end of tail
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # now return the list
        return tail.next


llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()
