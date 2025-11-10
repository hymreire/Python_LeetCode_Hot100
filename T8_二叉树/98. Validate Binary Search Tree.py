# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## 很好的题目
# 一道题搞定了三种遍历方式
# 有时间可以把中序遍历再复习一遍
# 现在完全可以写了

# 前序遍历：根左右
# 上下界这个想法比较巧妙
class Solution:
    def isValidBST(self, root: Optional[TreeNode],left=-inf,right=inf) -> bool:
        if root is None:
            return True
        x=root.val
        return left<x<right and \
                self.isValidBST(root.left,left,x) and \
                self.isValidBST(root.right,x,right)

# 中序遍历：左根右
# 维护一个全局变量，用于进行下一次比较（中序遍历这么做完全可以，因为是左根右，右会与下一个左比较）
class Solution:
    pre=-inf # 感觉这个pre写在外面很危险，最好还是多写个dfs，pre放在里面比较好
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val<=self.pre:
            return False
        self.pre=root.val
        return self.isValidBST(root.right)

# 后续遍历：左右根
# 递归，自底而上
# 这里的上下界比较难
# 全局max、min值是因为搜索树必须大于全部左子树，小于全部右子树
# 逐支遍历会使得左子树的右节点无法当前根节点比较
# 也就是说root.left.right>root.left，但是root和root.left.right无法比较
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(r):
            if r is None:
                return inf,-inf # 安全值：inf使得rmin满足要求，-inf使得lmax满足要求
            lmin,lmax=dfs(r.left)
            rmin,rmax=dfs(r.right)
            x=r.val
            if x<=lmax or x>=rmin:
                return -inf,inf # 死亡值：-inf使得rmin违法，inf使得lmax违法
            return min(lmin,x),max(rmax,x) # 更新当前子树的最小最大值
        return dfs(root)[1]!=inf # 无论哪一只违法，最后一定会演变为：上界-inf，下界inf
