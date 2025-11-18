# 2090. K Radius Subarray Averages

# 滑动窗口：入、更新、出
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        ans=[-1 for _ in range(n)]
        left=right=0
        tmp=0
        for right,x in enumerate(nums):
            tmp+=x
            if right-left<2*k:
                continue
            mid=(left+right)//2
            ans[mid]=tmp//(2*k+1)
            tmp-=nums[left]
            left+=1
        return ans

# 时间复杂度O(n)，空间复杂度O(1)