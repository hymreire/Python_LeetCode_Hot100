# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=tmp=0
        ans=inf
        for right,enter in enumerate(nums):
            tmp+=enter
            if tmp<target:
                continue
            while tmp-nums[left]>=target: # 这步比较重要
                tmp-=nums[left]
                left+=1
            ans=min(ans,right-left+1)
        return ans if ans<inf else 0
# 时间复杂度O(n)、空间复杂度O(1)