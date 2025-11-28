# 713. Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: # 严格小于
            return 0
        ans=left=0
        prod=1
        # 滑动窗口
        for right,x in enumerate(nums):
            prod*=x
            while prod>=k:
                prod//=nums[left]
                left+=1
            ans+=right-left+1 # 关键点：固定右端点更新答案
        return ans
# 时间复杂度：O(n)
# 空间复杂度：O(1)