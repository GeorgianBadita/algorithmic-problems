# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    if not head:
        return

    first_pointer = head
    curr_pointer = head

    while k >= 0 and first_pointer is not None:
        first_pointer = first_pointer.next
        k -= 1

    if k == 0:
        head = head.next
        return

    while first_pointer is not None:
        first_pointer = first_pointer.next
        curr_pointer = curr_pointer.next

    curr_pointer.next = curr_pointer.next.next
