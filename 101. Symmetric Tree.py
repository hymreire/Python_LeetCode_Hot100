# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
# 自底向上，递归判断两个子树是否对称
class Solution:
    def same2(self,r1,r2):
        if r1 is None or r2 is None:
            return r1 is r2
        return r1.val==r2.val and self.same2(r1.left,r2.right) and self.same2(r1.right,r2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.same2(root.left,root.right)