# 3634. Minimum Removals to Balance Array

# 排序+滑动窗口
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort() # 排序：O(n*log(n))
        left=ans=0
        for right,enter in enumerate(nums):
            outer=nums[left]
            while enter/outer>k:
                left+=1
                outer=nums[left]
            ans=max(ans,right-left+1)
        ans=len(nums)-ans # 题目要求的是删除的数量
        return ans
# 时间复杂度：O(n*log(n))、空间复杂度O(1)