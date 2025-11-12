# 114. Flatten Binary Tree to Linked List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## 这道题思路有点难，可以先背下来

# 递归，头插法
class Solution:
    head=None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left=None
        root.right=self.head
        self.head=root

# 递归，分治法
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        lt=self.flatten(root.left)
        rt=self.flatten(root.right)
        if lt:
            lt.right=root.right
            root.right=lt
            root.left=None
        return rt or lt or root # 尾节点优先选右，次选左，最次选根