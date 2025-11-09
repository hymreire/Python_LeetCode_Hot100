# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        m=len(nums)//2 # 神来之笔
        left=self.sortedArrayToBST(nums[:m])
        right=self.sortedArrayToBST(nums[m+1:])
        return TreeNode(nums[m],left,right)