# 199. Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(r,d):
            if r is None:
                return
            nonlocal ans
            if len(ans)==d:
                ans.append(r.val)
            dfs(r.right,d+1)
            dfs(r.left,d+1)
        dfs(root,0)
        return ans

# 自己写的前序遍历（根左右）
# 其实方法和灵神给的也差不了太多，时间复杂度大概是高于他。。。
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(r,d):
            if r is None:
                return
            nonlocal ans
            if len(ans)<=d:
                ans.append(r.val)
            else:
                ans[d]=r.val
            dfs(r.left,d+1)
            dfs(r.right,d+1)
        dfs(root,0)
        return ans