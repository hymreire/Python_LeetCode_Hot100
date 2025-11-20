# 2958. Length of Longest Subarray With at Most K Frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=left=0
        cnt=defaultdict(int)
        for right,num in enumerate(nums):
            cnt[num]+=1
            while cnt[num]>k:
                outer=nums[left]
                cnt[outer]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
# 时间复杂度O(n)、空间复杂度O(n)