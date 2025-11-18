# 643. Maximum Average Subarray I

# 滑动窗口
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=tmp=0 # ans可以设置为-inf
        left=0 # 可以不设置left
        for right,x in enumerate(nums):
            tmp+=x
            if right-left==k-1:
                ans=tmp
            elif right-left>k-1:
                tmp-=nums[left]
                left+=1
                ans=max(ans,tmp)
        return ans/k

# 时间复杂度：O(n)、空间复杂度：O(1)