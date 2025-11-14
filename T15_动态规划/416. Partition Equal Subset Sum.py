# 416. Partition Equal Subset Sum

# 递归，记忆化搜索
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> bool:
            if i < 0:
                return j == 0
            if j < nums[i]:
                return dfs(i - 1, j)  # 只能不选
            return dfs(i - 1, j - nums[i]) or dfs(i - 1, j)  # 选或不选

        s = sum(nums)
        return s % 2 == 0 and dfs(len(nums) - 1, s // 2)

# 简化写法
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> bool:
            if i < 0:
                return j == 0
            return j >= nums[i] and dfs(i - 1, j - nums[i]) or dfs(i - 1, j)

        s = sum(nums)
        return s % 2 == 0 and dfs(len(nums) - 1, s // 2)

# 递推
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s //= 2  # 注意这里把 s 减半了
        n = len(nums)
        f = [[False] * (s + 1) for _ in range(n + 1)] # 使用前i个元素，能否凑出j
        f[0][0] = True # 前0个元素（空集）可以凑出0（空集就是都不选）
        for i, x in enumerate(nums):
            for j in range(s + 1):
                f[i + 1][j] = j >= x and f[i][j - x] or f[i][j] # 选或不选
        return f[n][s]

# 空间优化，一个数组
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s //= 2  # 注意这里把 s 减半了
        f = [True] + [False] * s
        s2 = 0
        for i, x in enumerate(nums):
            s2 = min(s2 + x, s) # 理论上此时能达到的最大值
            for j in range(s2, x - 1, -1): # 只考虑j>=x的情况
                f[j] = f[j] or f[j - x] # 选或不选
            if f[s]: # 如果能凑出s，则返回True
                return True
        return False # 如果遍历完所有元素，都不能凑出s，则返回False

# 位集合
# 难度比较高，可以不背
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s //= 2
        f = 1 # 二进制，第i位为1表示能凑出i
        for x in nums:
            f |= f << x # 选或不选
        return (f >> s & 1) == 1