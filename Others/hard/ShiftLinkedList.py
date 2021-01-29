def shiftLinkedList(head, k):
    if not head or not head.next:
        return head

    list_len = 0
    hd_cpy = head
    while hd_cpy != None:
        list_len += 1
        hd_cpy = hd_cpy.next

    k = k % list_len
    current_pointer = head
    for _ in range(k):
        current_pointer = current_pointer.next

    curr_head = head
    while current_pointer.next != None:
        curr_head = curr_head.next
        current_pointer = current_pointer.next
    current_pointer.next = head
    head = curr_head.next
    curr_head.next = None
    return head


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
