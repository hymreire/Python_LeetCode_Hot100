# 62. Unique Paths

# 递归，记忆化搜索
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)

# 递推
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建 (m+1) x (n+1) 的 DP 表，f[i+1][j+1] 表示到达网格位置 (i, j) 的路径数
        f = [[0] * (n + 1) for _ in range(m + 1)]
        # 初始化基准值：f[0][1] = 1 或 f[1][0] = 1 都可以
        # 这样当计算 f[1][1] = f[0][1] + f[1][0] 时，能得到正确的初始值 1
        f[0][1] = 1
        for i in range(m):
            for j in range(n):
                f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j]
        return f[m][n]

# 空间优化
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [0] * (n + 1)
        f[1] = 1
        for _ in range(m):
            for j in range(n):
                f[j + 1] += f[j] # 对应递推公式
        return f[n]

# 组合
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)