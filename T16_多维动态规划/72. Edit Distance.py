# 72. Edit Distance

# 递归，记忆化搜索
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if s[i] == t[j]:
                return dfs(i - 1, j - 1)
            # 当 s[i] != t[j] 时，有三种操作方式：
            # 1. dfs(i - 1, j): 删除 s[i]，让 s[0:i-1] 匹配 t[0:j]
            #    操作：删除 s 的第 i 个字符，然后让 s[0:i-1] 匹配 t[0:j]
            # 2. dfs(i, j - 1): 插入 t[j] 到 s[i] 之后，让 s[0:i] 匹配 t[0:j-1]
            #    操作：在 s 的第 i+1 索引位置插入 t[j]，然后让 s[0:i] 匹配 t[0:j-1]
            # 3. dfs(i - 1, j - 1): 替换 s[i] 为 t[j]，让 s[0:i-1] 匹配 t[0:j-1]
            #    操作：将 s[i] 替换为 t[j]，然后让 s[0:i-1] 匹配 t[0:j-1]
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1
        return dfs(n - 1, m - 1)

# 递推及其优化方法
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0] = list(range(m + 1))
        for i, x in enumerate(s):
            f[i + 1][0] = i + 1
            for j, y in enumerate(t):
                f[i + 1][j + 1] = f[i][j] if x == y else \
                        min(f[i][j + 1], f[i + 1][j], f[i][j]) + 1
        return f[n][m]

class Solution:
    def minDistance(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [list(range(m + 1)), [0] * (m + 1)]
        for i, x in enumerate(s):
            f[(i + 1) % 2][0] = i + 1
            for j, y in enumerate(t):
                f[(i + 1) % 2][j + 1] = f[i % 2][j] if x == y else \
                        min(f[i % 2][j + 1], f[(i + 1) % 2][j], f[i % 2][j]) + 1
        return f[n % 2][m]

class Solution:
    def minDistance(self, s: str, t: str) -> int:
        f = list(range(len(t) + 1))
        for x in s:
            pre = f[0]
            f[0] += 1  # f[0] = i + 1
            for j, y in enumerate(t):
                tmp = f[j + 1]
                f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
                pre = tmp
        return f[-1]