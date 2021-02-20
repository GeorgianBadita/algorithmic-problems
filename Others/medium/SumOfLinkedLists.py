# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    result_list = None
    head = None
    carry = 0

    while linkedListOne or linkedListTwo:
        first = 0 if not linkedListOne else linkedListOne.value
        second = 0 if not linkedListTwo else linkedListTwo.value

        result = first + second + carry
        carry = result // 10
        result = result % 10

        if not result_list:
            result_list = LinkedList(result)
            head = result_list
        else:
            result_list.next = LinkedList(result)
            result_list = result_list.next

        linkedListOne = linkedListOne.next if linkedListOne else None
        linkedListTwo = linkedListTwo.next if linkedListTwo else None

    if carry:
        result_list.next = LinkedList(1)
    return head
