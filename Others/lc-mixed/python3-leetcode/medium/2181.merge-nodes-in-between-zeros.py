from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_zero_ptr = head
        ret_head = head
        curr_value = None
        # head = [4,3,1,0,4,5,2,0]

        while head:
            if head.val != 0:
                curr_value += head.val
                head = head.next
            else:
                if curr_value != None:
                    tmp = last_zero_ptr
                    tmp.val = curr_value
                    last_zero_ptr.next = head
                    last_zero_ptr = head
                    head = head.next
                    curr_value = 0
                else:
                    curr_value = 0
                    head = head.next
        last_zero_ptr.next = None
        return ret_head


ll = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))

sol = Solution().mergeNodes(ll)

print(sol)