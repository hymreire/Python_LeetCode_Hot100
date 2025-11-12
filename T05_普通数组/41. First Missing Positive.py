# 41. First Missing Positive

# 方法：换座位法
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]: # 反复处理当前索引直到当前索引直到当前索引满足要求或者无法满足要求
                j=nums[i]-1
                nums[i],nums[j]=nums[j],nums[i] # 交换元素，把nums[i]放到正确的位置
        for i in range(n): # 判断i元素是不是等于i+1
            if nums[i]!=i+1:
                return i+1
        return n+1