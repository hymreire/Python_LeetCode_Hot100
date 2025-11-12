# 238. Product of Array Except Self

# 方法一：前后缀分解
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*n # 表示0到i-1的乘积
        suf=[1]*n # 表示i+1到n-1的乘积
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            suf[i]=suf[i+1]*nums[i+1]
        return [p*s for p,s in zip(pre,suf)]

# 空间优化
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        suf=[1]*n
        for i in range(n-2,-1,-1):
            suf[i]=suf[i+1]*nums[i+1]
        pre=1
        for i,x in enumerate(nums):
            suf[i]=pre*suf[i]
            pre*=x
        return suf