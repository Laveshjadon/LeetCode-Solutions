# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        curr = head 
        count = 0 
        while curr and count < k:
            curr = curr.next 
            count += 1
        if count == k:
            curr = head
            prev = None
            

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            head.next = self.reverseKGroup(curr, k)
            return prev
        return head
        