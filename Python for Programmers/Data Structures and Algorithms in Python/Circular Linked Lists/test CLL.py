def is_circular_linked_list(self, input_list):
    # check if not empty
    if input_list.head:
        cur = input_list.head
        # traverse till curr.next is None
        while cur.next:
            cur = cur.next
            # if any node points back to head then CLL exists
            if cur.next == input_list.head:
                return True
        # if curr.next becomes None it means not CLL
        return False
    else:
        return False
