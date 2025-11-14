# 75. Sort Colors

# 插入排序
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0 = p1 = 0 # 双指针，p0指向0的末尾，p1指向1的末尾
        for i, x in enumerate(nums):
            nums[i] = 2 # 2永远占据最右
            if x <= 1: # 如果是1插入和右移没问题，如果是0则会覆盖1的位置，因此必须插入右移保持不动
                nums[p1] = 1
                p1 += 1
            if x == 0: # 如果x==0，则x是0，p0指针右移
                nums[p0] = 0
                p0 += 1