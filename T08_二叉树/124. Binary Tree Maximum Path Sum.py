# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归，树形DP
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=-inf
        def dfs(r): # 这个函数返回的是不可拐弯的最大链的和而非可以拐弯的路径的和
            if r is None:
                return 0
            left=dfs(r.left)
            right=dfs(r.right)
            nonlocal ans
            ans=max(left+right+r.val,ans)
            return max(max(left,right)+r.val,0) # 空集的和为0，小于这个就别选链了
        dfs(root)
        return ans