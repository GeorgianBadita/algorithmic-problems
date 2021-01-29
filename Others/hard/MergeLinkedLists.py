# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    if not headOne:
        return headTwo

    if not headTwo:
        return headOne

    if headOne.value > headTwo.value:
        headTwo, headOne = headOne, headTwo

    head1_cpy = headOne
    head2_cpy = headTwo

    while head1_cpy and head2_cpy:
        current_head2_val = head2_cpy.value
        current_head1_val = head1_cpy.value

        if current_head2_val >= current_head1_val:
            if not head1_cpy.next:
                head1_cpy.next = LinkedList(current_head2_val)
                head2_cpy = head2_cpy.next
            else:
                if head1_cpy.next.value >= current_head2_val:
                    nxt_head = LinkedList(current_head2_val)
                    nxt_head.next = head1_cpy.next
                    head1_cpy.next = nxt_head
                    head1_cpy = nxt_head
                    head2_cpy = head2_cpy.next
                else:
                    head1_cpy = head1_cpy.next
        else:
            head1_cpy = head1_cpy.next

    return headOne


h1 = LinkedList(2)
h1.next = LinkedList(6)
h1.next.next = LinkedList(7)
h1.next.next.next = LinkedList(8)

h2 = LinkedList(1)
h2.next = LinkedList(3)
h2.next.next = LinkedList(4)
h2.next.next.next = LinkedList(5)
h2.next.next.next.next = LinkedList(9)
h2.next.next.next.next.next = LinkedList(10)

mergeLinkedLists(h1, h2)
