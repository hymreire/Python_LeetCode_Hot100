# W476_Q2

# 思路：可以推导出，ab一定会全部消掉

# "aabbab"

# 我的解答：观察出性质后用Counter解决非常方便
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        cnt=Counter(s)
        return abs(cnt['a']-cnt['b'])

# 灵神解答：本质是一样的
# 脑筋急转弯
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        return abs(s.count('a') * 2 - len(s))