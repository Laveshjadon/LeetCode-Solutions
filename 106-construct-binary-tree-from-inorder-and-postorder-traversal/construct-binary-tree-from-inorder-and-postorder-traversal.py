# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder and not postorder:
            return None 
        hassh ={}
        for i in range(len(inorder)):
            hassh[inorder[i]] = i
        self.idx = -1
        def bst(left,right):
            if left > right:
                return None
            value = postorder[self.idx]
            self.idx -= 1
            mid = hassh[value]
            root = TreeNode(value)
            root.right = bst(mid+1,right)
            root.left = bst(left,mid-1)
            
            return root
        return bst(0,len(inorder)-1)


        