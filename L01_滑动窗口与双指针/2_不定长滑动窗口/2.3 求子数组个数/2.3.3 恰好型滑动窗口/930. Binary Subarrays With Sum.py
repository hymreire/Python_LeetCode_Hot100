# 930. Binary Subarrays With Sum

class Solution:
    def numLeast(self, nums, k): # 和至少为k
        ans=left=s=0
        for right,n in enumerate(nums):
            s+=n
            while s>=k and left<=right:
                s-=nums[left]
                left+=1
            ans+=left
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int: # 和恰好为goal
        return self.numLeast(nums,goal)-self.numLeast(nums,goal+1) # 和至少为goal-和至少为goal+1==和恰好为goal
# 时间复杂度：O(n)
# 空间复杂度：O(1)