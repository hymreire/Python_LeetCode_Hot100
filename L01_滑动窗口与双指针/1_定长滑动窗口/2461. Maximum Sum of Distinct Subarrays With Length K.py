# 2461. Maximum Sum of Distinct Subarrays With Length K

# 滑动窗口
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans=s=t=left=0 # 简洁写法
        cnt=defaultdict(int)
        for right,enter in enumerate(nums):
            s+=enter
            cnt[enter]+=1
            if cnt[enter]==1:
                t+=1
            if right-left<k-1:
                continue
            if t==k:
                ans=max(ans,s)
            outer=nums[left]
            s-=outer
            cnt[outer]-=1
            if cnt[outer]==0:
                t-=1
            left+=1
        return ans