# W476_Q1

from turtle import left
from typing import AnyStr
from typing import List

# 思路：减应该选最小的那个索引，加应该选最大的那两个索引
# 选最小的那个索引

# 感觉这个不太好，压根不算算法，后面看看能不能再做优化

class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        n=len(nums)
        min=nums[0]
        min_idx=0
        for i in range(n):
            if nums[i]<min:
                min=nums[i]
                min_idx=i
        max=nums[0]
        max_idx=0
        for i in range(n):
            if nums[i]>max and i!=min_idx:
                max=nums[i]
                max_idx=i
        max2=min
        max2_idx=0
        for i in range(n):
            if nums[i]>max2 and i!=max_idx and i!=min_idx:
                max2=nums[i]
        return max+max2-min

# 灵神解法：
# 排序，简洁明快
class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] + nums[-2] - nums[0]

# 时间优化
class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        return sum(nlargest(2, nums)) - min(nums) # 堆函数，找到最大的两个值 # 可以背一下这个API，时间复杂度更低
        
        

if __name__ == "__main__":
    solution=Solution()
    print(solution.maximizeExpressionOfThree([-4,-8,-10]))