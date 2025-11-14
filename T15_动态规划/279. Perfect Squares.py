# 279. Perfect Squares

# 递归，记忆化搜索
# 写在外面，多个测试数据之间可以共享，减少计算量
@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
def dfs(i: int, j: int) -> int:
    if i == 0:
        return inf if j else 0
    if j < i * i:
        return dfs(i - 1, j)  # 只能不选
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)  # 不选 vs 选
class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n) # 整数平方根

# 递推
N = 10000 # 类似记忆化搜索的cache，避免重复计算
f = [[0] * (N + 1) for _ in range(isqrt(N) + 1)]
f[0] = [0] + [inf] * N
for i in range(1, len(f)):
    for j in range(N + 1):
        if j < i * i:
            f[i][j] = f[i - 1][j]  # 只能不选
        else:
            f[i][j] = min(f[i - 1][j], f[i][j - i * i] + 1)  # 不选 vs 选
class Solution:
    def numSquares(self, n: int) -> int:
        return f[isqrt(n)][n]  # 也可以写 f[-1][n]

# 递推，空间优化
N = 10000
f = [0] + [inf] * N
for i in range(1, isqrt(N) + 1):
    for j in range(i * i, N + 1): # 从i*i开始可以避免越界
        f[j] = min(f[j], f[j - i * i] + 1)  # 不选 vs 选
class Solution:
    def numSquares(self, n: int) -> int:
        return f[n]