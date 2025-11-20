# 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        f0=left=ans=0
        for right,num in enumerate(nums):
            if num==0:
                f0+=1
            while f0>k:
                outer=nums[left]
                if outer==0:
                    f0-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
# 时间复杂度O(n)、空间复杂度O(1)