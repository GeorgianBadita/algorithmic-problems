#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revert_list(self, head):
        curr = None
        head_cpy = head
        while head_cpy:
            tmp = head_cpy.next
            head_cpy.next = curr
            curr = head_cpy
            head_cpy = tmp
        return curr

    def find_mid_node(self, head):
        before_mid = None
        slow = head
        fast = head
        while fast and fast.next:
            before_mid = slow
            slow = slow.next
            fast = fast.next.next
        return before_mid

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        before_mid = self.find_mid_node(head)
        mid = before_mid.next
        before_mid.next = None
        rev_head = self.revert_list(mid)

        p1, p2 = head, rev_head

        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
        # @lc code=end
