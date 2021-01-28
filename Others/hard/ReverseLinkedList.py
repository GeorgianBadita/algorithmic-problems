def reverseLinkedList(head):
    if not head or not head.next:
        return head

    current = None
    pointer = head

    while pointer is not None:
        tmp = pointer.next
        pointer.next = current
        current = pointer
        pointer = tmp

    return current
