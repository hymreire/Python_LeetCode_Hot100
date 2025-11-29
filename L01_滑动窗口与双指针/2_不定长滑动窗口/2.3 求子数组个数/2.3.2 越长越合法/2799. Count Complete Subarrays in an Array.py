# 2799. Count Complete Subarrays in an Array

# python set: https://www.runoob.com/python3/python3-set.html
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        diff=len(set(nums)) # 用集合计算长度会更快一些
        ans=left=0
        res=defaultdict(int)
        for n in nums:
            res[n]+=1
            while len(res)>=diff:
                outer=nums[left]
                res[outer]-=1
                if res[outer]==0:
                    del res[outer]
                left+=1
            ans+=left
        return ans
# 时间复杂度：O(n)
# 空间复杂度：O(diff)