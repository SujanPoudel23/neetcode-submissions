# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestorRec(self, node, target, ancestorList):
        if node is None:
            return ancestorList
        
        if target == node.val:
            ancestorList.append(node)
            return ancestorList
        elif target > node.val:
            ancestorList.append(node)
            self.lowestCommonAncestorRec(node.right, target, ancestorList)
        else:
            ancestorList.append(node)
            self.lowestCommonAncestorRec(node.left, target, ancestorList)


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_list = []
        q_list = []
        findP = self.lowestCommonAncestorRec(root, p.val, p_list)
        findQ = self.lowestCommonAncestorRec(root, q.val, q_list)
        
        highest = root.val
        for i in range(min(len(p_list), len(q_list))):
            if q_list[i].val == p_list[i].val:
                highest = p_list[i]
            else:
                return highest
        
        return highest
        
        