# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    if not linkedList or not linkedList.next:
        return linkedList

    distinct_pointer = linkedList
    current_pointer = linkedList

    while current_pointer:
        if current_pointer.value != distinct_pointer.value:
            distinct_pointer.next = current_pointer
            distinct_pointer = current_pointer

        current_pointer = current_pointer.next
    pointer = linkedList
    while pointer and pointer.next and pointer.value != pointer.next.value:
        pointer = pointer.next
    pointer.next = None

    return linkedList
