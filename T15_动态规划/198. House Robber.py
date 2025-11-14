# 198. House Robber

# 记忆化搜索
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dfs(i) 表示从 nums[0] 到 nums[i] 最多能偷多少
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> int:
            if i < 0:  # 递归边界（没有房子）
                return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])

        return dfs(len(nums) - 1)  # 从最后一个房子开始思考

# 递推
class Solution:
    def rob(self, nums: List[int]) -> int:
        f = [0] * (len(nums) + 2) # 前两个位置等价于递归的-1和-2，初始化为0即可
        for i, x in enumerate(nums):
            f[i + 2] = max(f[i + 1], f[i] + x)
        return f[-1]

# 空间优化，需要背下来
class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
             # 指针右移，新f0就是旧f1，而新f1需要由递推公式取最大值计算
             # 可以假设旧的f1就是对的，而新的f1需要由旧的真值计算
            f0, f1 = f1, max(f1, f0 + x)
        return f1