# 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=ans=0
        cnt=defaultdict(int)
        for right,num in enumerate(nums):
            cnt[num]+=1
            while cnt[0]>1:
                outer=nums[left]
                cnt[outer]-=1
                left+=1
            ans=max(ans,right-left)
        return ans
# 时间复杂度O(n)、空间复杂度O(1)