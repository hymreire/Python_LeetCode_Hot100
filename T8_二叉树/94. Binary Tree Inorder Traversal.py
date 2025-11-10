# 94. Binary Tree Inorder Traversal

# 这道题灵神没给题解，先看一下官解，等以后读懂灵神其他解法，再把官解替掉

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.inorder(root,res)
        return res
    def inorder(self,root,res):
        if root is None:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)

# 迭代
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stk=[]
        while root or stk:
            while root:
                stk.append(root)
                root=root.left
            root=stk.pop()
            res.append(root.val)
            root=root.right # 直接转右，判断条件非常强大
        return res

# Morris 遍历，官解转Python
# 图解倒是可以理解为什么这么做
# 但是背下来还是很有难度
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 步骤 2: 初始化
        res = []
        # 步骤 3: 核心迭代
        while root:
            # 步骤 4: 调整判断条件
            # 情况 A: 没有左子树 (LDR -> DR)
            if not root.left:
                res.append(root.val) # D
                root = root.right    # R
            # 情况 B: 有左子树
            else:
                # 1. 找到前驱
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                # 2. 根据线索判断
                if not predecessor.right:
                    # 2a. (第一次到) 建立线索，然后深入 L
                    predecessor.right = root
                    root = root.left
                else: 
                    # 2b. (第二次到) L 已完成
                    res.append(root.val)      # 访问 D
                    predecessor.right = None  # 拆除线索
                    root = root.right         # 深入 R
        # 步骤 1: 返回结果
        return res

# 按照灵神的中序遍历写法整了一下，感觉和gemini的官解转python也没啥区别：
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(r):
            if r is None:
                return
            dfs(r.left)
            nonlocal ans
            ans.append(r.val)
            dfs(r.right)
        dfs(root)
        return ans