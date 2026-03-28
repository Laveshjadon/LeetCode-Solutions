# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        curr = head
        arr = []
        while odd:
            arr.append(odd.val)
            odd = odd.next.next if odd.next else None
        while even:
            arr.append(even.val)
            even = even.next.next if even.next else None
        for val in arr:
            curr.val = val
            curr = curr.next
        return head

        