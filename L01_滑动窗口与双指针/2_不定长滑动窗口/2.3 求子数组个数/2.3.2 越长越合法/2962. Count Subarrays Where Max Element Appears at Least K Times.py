# 2962. Count Subarrays Where Max Element Appears at Least K Times

# 大循环滑动右端点
# 小循环滑动左端点
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans=0
        left=0 # 初始化为0
        cnt=0
        maxn=max(nums) # 重点是最大元素出现的次数
        for right,enter in enumerate(nums):
            if enter==maxn:
                cnt+=1
            while cnt>=k:
                outer=nums[left]
                if outer==maxn:
                    cnt-=1
                left+=1
            ans+=left # 从内循环看，固定右端点
        return ans
# 时间复杂度：O(n)
# 空间复杂度：O(1)