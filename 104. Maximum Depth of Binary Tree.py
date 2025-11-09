# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
# 这道题就是递归的入门题

# 自底向上
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ld=self.maxDepth(root.left)
        rd=self.maxDepth(root.right)
        return max(ld,rd)+1 # 存在节点至少有一个深度

# 自顶向下
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(r,d):
            nonlocal ans
            if r is None:
                return
            d+=1
            ans=max(ans,d)
            # 这题就没有返回值，当前深度算完继续向下遍历就行
            dfs(r.left,d)
            dfs(r.right,d)
        dfs(root,0)
        return ans