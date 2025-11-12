# 33. Search in Rotated Sorted Array

# 二分法：1、有理由的变更指针；【结合实际，强行终止】2、避免越界【结合特值，确定如何终止以及返回谁】

# 两次二分，闭区间（这个方法是真麻烦，学一道相当于学三道了）
# 旋转数组最小值
def FindMin(nums):
    left,right=0,len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<=nums[-1]: # 第二支
            right=mid-1
        else:
            left=mid+1
    return left
# 升序数组最小值
def LowerBound(nums,target,left,right):
    UpperBound=right+1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left if left<UpperBound and nums[left]==target else -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 先确定旋转数组最小值所在的索引
        index=FindMin(nums)
        # 如果目标值大于等于索引-1对应的数字，缩小区间
        if target>nums[-1]:
            return LowerBound(nums,target,0,index-1)
        else:
            return LowerBound(nums,target,index,len(nums)-1)

# 一次二分
# 判定条件我完全是用特例逼出的，理论不好推导
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            x=nums[mid]
            if x<=nums[-1]<target: # x在第二支，target在第一支，右指针要往左逼
                right=mid-1
            elif target<=nums[-1]<x: # target在第二支，x在第一支，左指针要往右逼
                left=mid+1
            elif x<target: # 同一支，x小于target
                left=mid+1
            elif target<=x: # 同一支，x大于target
                right=mid-1
        return left if left<len(nums) and nums[left]==target else -1

# 
