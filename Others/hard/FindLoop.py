# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):

    tortoise = head.next
    hare = head.next.next

    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next

    tortoise = head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next

    return tortoise
