# 189. Rotate Array

# 反转数组法：这个思路比较巧妙，但是感觉不容易想到
# 而且如果要用反转函数，感觉原地操作好像还更快一点
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        n=len(nums)
        k=k%n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)

# Python切片解法还是很简单，但是灵神不推荐这种解法
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路：这题用python撑死一步
        n=len(nums)
        k=k%n
        nums[:k],nums[k:]=nums[n-k:],nums[:n-k]