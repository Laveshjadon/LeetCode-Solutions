# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        dum_bf = ListNode(0)
        dum_tail = dum_bf

        dum_af = ListNode(0)
        dumaf_tail = dum_af

        curr = head
        while curr:
            if curr.val < x:
                dum_tail.next  = curr
                dum_tail = dum_tail.next
            else:
                dumaf_tail.next = curr
                dumaf_tail = dumaf_tail.next
            curr = curr.next
        dumaf_tail.next = None
        dum_tail.next = dum_af.next 
        return dum_bf.next
                

                
                
        