# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代，利用前序的根左右和中序的左根右，将树拆成左和右
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        left_size=inorder.index(preorder[0]) # 返回根节点在inorder中的索引，其实也是左树的长度
        left=self.buildTree(preorder[1:1+left_size],inorder[:left_size])
        right=self.buildTree(preorder[1+left_size:],inorder[1+left_size:])
        return TreeNode(preorder[0],left,right) # 构造树

# 哈希表
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index={x:i for i,x in enumerate(inorder)}
        def dfs(pre_l,pre_r,ino_l,ino_r):
            if pre_l==pre_r:
                return
            left_size=index[preorder[pre_l]]-ino_l
            # 确定pre和ino的左右区间
            # 前序的左右区间好写，从当前节点往右边数即可
            # 中序的左右区间难写，左区间是左边界到索引，右区间是索引到右边界
            left=dfs(pre_l+1,pre_l+1+left_size,ino_l,ino_l+left_size)
            right=dfs(pre_l+1+left_size,pre_r,ino_l+left_size+1,ino_r)
            return TreeNode(preorder[pre_l],left,right)
        return dfs(0,len(preorder),0,len(inorder))