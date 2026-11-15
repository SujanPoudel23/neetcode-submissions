# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBSTRec(self, node, minN, maxN):
        if node is None:
            return True
        
        if node.val <= minN or node.val >= maxN:
            return False

        return self.isValidBSTRec(node.left, minN, node.val) and self.isValidBSTRec(node.right, node.val, maxN)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None

        return self.isValidBSTRec(root, -math.inf, math.inf)