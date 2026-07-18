# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head and right == left:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        start = prev.next
        curr = start 
        prev_res = None
        for _ in range(right-left+1):
            nxt = curr.next
            curr.next = prev_res
            prev_res = curr
            curr = nxt

        prev.next = prev_res
        start.next = curr
        return dummy.next



        