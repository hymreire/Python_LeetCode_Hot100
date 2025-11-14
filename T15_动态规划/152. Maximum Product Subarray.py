# 152. Maximum Product Subarray

# 动态规划
# 这个真好背
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f_max = [0] * n # 以i结尾的乘积最大子数组
        f_min = [0] * n # 以i结尾的乘积最小子数组
        f_max[0] = f_min[0] = nums[0]
        for i in range(1, n):
            x = nums[i]
            # 把 x 加到右端点为 i-1 的（乘积最大/最小）子数组后面，
            # 或者单独组成一个子数组，只有 x 一个元素
            f_max[i] = max(f_max[i - 1] * x, f_min[i - 1] * x, x)
            f_min[i] = min(f_max[i - 1] * x, f_min[i - 1] * x, x)
        return max(f_max)

# 空间优化
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf  # 注意答案可能是负数
        f_max = f_min = 1 # 初始化乘积最大和最小子数组为1
        for x in nums:
            f_max, f_min = max(f_max * x, f_min * x, x), \
                           min(f_max * x, f_min * x, x)
            ans = max(ans, f_max)
        return ans

# 空间优化的另一种写法
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf
        f_max = f_min = 1
        for x in nums:
            if x < 0:
                # 下面与 x 相乘后，最大的正数变成最小的负数，最小的负数变成最大的正数
                # 提前交换，这样可以把 x < 0 和 x >= 0 的情况合并，合并后，计算 max 和 min 可以少一项
                f_max, f_min = f_min, f_max
            f_max = max(f_max * x, x)
            f_min = min(f_min * x, x)
            ans = max(ans, f_max)
        return ans