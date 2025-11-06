# 1. Two Sum

from typing import List # 类型提示

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx={} # 字典就是哈希表
        for j,x in enumerate(nums):
            if target-x in idx:
                return [idx[target-x],j]
            idx[x]=j

# 本地测试代码
if __name__ == "__main__": # main函数
    solution = Solution()
    
    # 测试用例 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"示例 1:")
    print(f"输入：nums = {nums1}, target = {target1}")
    print(f"输出：{result1}")
    print(f"解释：因为 nums[{result1[0]}] + nums[{result1[1]}] == {target1}，返回 {result1}")
    print()
    
    # 测试用例 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"示例 2:")
    print(f"输入：nums = {nums2}, target = {target2}")
    print(f"输出：{result2}")
    print()
    
    # 测试用例 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"示例 3:")
    print(f"输入：nums = {nums3}, target = {target3}")
    print(f"输出：{result3}")
    print()