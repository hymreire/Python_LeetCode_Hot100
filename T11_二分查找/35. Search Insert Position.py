# 35. Search Insert Position

# 二分法：其实硬背就行，实在过不了就找特值确定边界条件即可

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

# 左闭右开区间
def lower_bound(nums,target):
    left,right=0,len(nums)
    while left<right:
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid+1
        else:
            right=mid # 左闭右开右不动
    return left

# 开区间
def lower_bound(nums,target):
    left,right=-1,len(nums)
    while left+1<right:
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid
        else:
            right=mid
    return right

# 库函数（复杂的题目建议直接调库）
def lower_bound(nums,target):
    return bisect_left(nums,target)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return lower_bound(nums,target)