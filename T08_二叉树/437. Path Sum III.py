# 437. Path Sum III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS+前缀和（回溯）
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans=0
        cnt=defaultdict(int)
        cnt[0]=1 # 空集合算一种
        def dfs(r,s):
            nonlocal ans
            if r is None:
                return
            s+=r.val
            ans+=cnt[s-targetSum]
            cnt[s]+=1
            dfs(r.left,s)
            dfs(r.right,s)
            # 注意：这道题路径只能同一支，不能跨分支（也就是向下）
            cnt[s]-=1 # 撤销，为了遍历其他分支（比如当前树是左树，接下来遍历右树，左树的和用不上）
        dfs(root,0)
        return ans