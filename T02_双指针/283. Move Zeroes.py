# 283. Move Zeroes

# 方法1：栈
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack=0
        for x in nums:
            if x:
                nums[stack]=x
                stack+=1
        for i in range(stack,len(nums)):
            nums[i]=0

# 方法2：双指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0=0 # 左端点
        for i,x in enumerate(nums):
            if x:
                nums[i0],nums[i]=nums[i],nums[i0] # 遇到非空的i，则移到i0处，然后左端点+1
                i0+=1
# 极端情况：全是非0：则i和i0一起前进，交换相当于不交换
# 极端情况：第一个是0，则i前进，i0不动，后面遇到非0换到i0的位置