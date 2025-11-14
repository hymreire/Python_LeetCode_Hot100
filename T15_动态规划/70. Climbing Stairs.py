# 70. Climbing Stairs

# 递归，记忆化搜索
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i<=1:
                return 1
            return dfs(i-1)+dfs(i-2)
        return dfs(n)

# 递推，空间最优
class Solution:
    def climbStairs(self, n: int) -> int:
        f0,f1=1,1
        for _ in range(2,n+1):
            f0,f1=f1,f0+f1
        return f1

# 矩阵快速幂，时空最优
# a @ b，其中 @ 是矩阵乘法
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]

# a^n @ f0
def pow_mul(a: List[List[int]], n: int, f0: List[List[int]]) -> List[List[int]]:
    res = f0
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res

class Solution:
    def climbStairs(self, n: int) -> int:
        m = [[1, 1], [1, 0]]
        f0 = [[1], [0]]
        fn = pow_mul(m, n, f0)
        return fn[0][0]