# 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root):
            if root is None:
                return -1 # 后面的逻辑是提前预支一个1
            ll=dfs(root.left)+1
            rl=dfs(root.right)+1
            nonlocal ans
            ans=max(ans,ll+rl)
            return max(ll,rl)
        dfs(root)
        return ans