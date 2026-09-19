# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
       def dfs(node1,node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        if not dfs(node1.left,node2.left):
            return False
        if not dfs(node1.right,node2.right):
            return False
        return True
       return dfs(p,q)
       

        