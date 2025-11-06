# 1. Two Sum - ACM模式（完整输入输出）

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for j, x in enumerate(nums):
            if target - x in idx:
                return [idx[target - x], j]
            idx[x] = j
        return []

# ACM模式：从标准输入读取数据并输出结果
if __name__ == "__main__":
    solution = Solution()
    
    # ACM模式输入格式：
    # 第一行：数组元素（空格分隔），例如：2 7 11 15
    # 第二行：目标值 target，例如：9
    nums = list(map(int, input().split()))
    target = int(input())
    
    # 计算结果
    result = solution.twoSum(nums, target)
    
    # 输出结果（ACM模式通常只需要输出结果，不需要额外信息）
    # 格式：[0,1] 或 [1,2] 等
    print(result)
    
    # ========== 以下为本地测试版本（带提示信息）==========
    # 如果需要本地测试，可以使用下面的代码替换上面的部分：
    """
    print("请输入数组元素（用空格分隔）：")
    nums = list(map(int, input().split()))
    
    print("请输入目标值 target：")
    target = int(input())
    
    result = solution.twoSum(nums, target)
    print(f"输出：{result}")
    
    if result:
        print(f"验证：nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
    """

