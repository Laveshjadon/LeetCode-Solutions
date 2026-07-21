# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if k == 0 or not head or not head.next:
            return head 
        curr = head
        length = 1
        while curr.next:
            curr = curr.next 
            length += 1
            

        k = k % length
        if k == 0:
            return head
        
        curr.next = head 


        steps = length - k - 1
        new_tail = head 
        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None 
        return new_head






        
        