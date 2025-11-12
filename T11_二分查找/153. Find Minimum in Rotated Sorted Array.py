# 153. Find Minimum in Rotated Sorted Array

# 闭区间写法：例子[4 5 1 2 3]
# 这里的边界条件我举了一个单元素的特例来确定
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1 # 假设left在第一段或交界处，right在第二段或交界处
        while left<=right:
            mid=(left+right)//2 # 整除偏左
            if nums[mid]<=nums[-1]: # 说明mid在第二段，最小值一定在第二段，而且不会超过mid，right移到mid即可
                right=mid-1 # 强行越界
            else: # 说明mid在第一段，最小值一定在第二段，而且一定大于mid
                left=mid+1
        return nums[left]

# 库函数写法（很巧妙）
class Solution:
    def findMin(self, nums: List[int]) -> int:
        check=lambda i: nums[i]<nums[-1] # 将第一段全部置为0，第二段全部置为1，最后一个元素不动
        i=bisect_left(range(len(nums)-1),1,key=check) # 0在最前则置为1，返回索引0；0在其他位置，则前面置为0，后面置为1，也能找到正确答案
        return nums[i]