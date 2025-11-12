# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历

# 全局变量
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=0
        def dfs(r):
            nonlocal ans,k
            if r is None:
                return None
            dfs(r.left)
            k-=1
            if k==0:
                ans=r.val
            dfs(r.right)
        dfs(root)
        return ans

# 不使用全局变量
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(r):
            if r is None:
                return None
            res=dfs(r.left)
            if res!=None:
                return res
            nonlocal k
            k-=1
            if k==0:
                return r.val
            return dfs(r.right)
        return dfs(root)