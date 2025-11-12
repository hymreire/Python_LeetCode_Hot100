# 34. Find First and Last Position of Element in Sorted Array

# 闭区间写法
def lower_bound(nums,target):
    left,right=0,len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left

# 左闭右开区间写法和开区间写法这里暂时忽略，有时间再做补充

# 库函数写法
def lower_bound(nums,target):
    return bisect_left(nums,target)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i,j=lower_bound(nums,target),lower_bound(nums,target+1)-1
        if i==len(nums) or nums[i]!=target:
            return [-1,-1]
        else:
            return [i,j]