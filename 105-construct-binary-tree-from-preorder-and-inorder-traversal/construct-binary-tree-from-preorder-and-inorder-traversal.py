# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        hassh = {}
        for i in range(len(inorder)):
            hassh[inorder[i]] = i
        self.idx = 0
        def bst(left,right):
            if left > right:
                return None
            value = preorder[self.idx]
            mid = hassh[value]
            self.idx += 1
            root = TreeNode(value)
            root.left= bst(left,mid - 1)
            root.right = bst(mid+1,right)
            return root
        return bst(0,len(inorder) - 1)