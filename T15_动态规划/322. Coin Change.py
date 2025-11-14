# 322. Coin Change

# 递归，记忆化搜索
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, c: int) -> int: # i: 当前硬币索引，c: 当前金额
            if i < 0:
                return 0 if c == 0 else inf
            if c < coins[i]:  # 只能不选
                return dfs(i - 1, c)
            # 不选 vs 继续选
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        ans = dfs(len(coins) - 1, amount)
        return ans if ans < inf else -1

# 递推
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[inf] * (amount + 1) for _ in range(n + 1)] # 索引0表示没有硬币的情况（除00为0，其余皆为inf）
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
        ans = f[n][amount]
        return ans if ans < inf else -1

# 递推，空间优化，两个数组
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[inf] * (amount + 1) for _ in range(2)]
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[(i + 1) % 2][c] = f[i % 2][c] # 两个数组轮流使用
                else:
                    f[(i + 1) % 2][c] = min(f[i % 2][c], f[(i + 1) % 2][c - x] + 1)
        ans = f[n % 2][amount]
        return ans if ans < inf else -1

# 递推，空间优化，一个数组
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [0] + [inf] * amount # 索引0表示没有硬币
        for x in coins:
            for c in range(x, amount + 1):
                f[c] = min(f[c], f[c - x] + 1) # 选或不选
        ans = f[amount]
        return ans if ans < inf else -1