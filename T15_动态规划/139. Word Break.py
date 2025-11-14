# 139. Word Break

# 递归，记忆化搜索
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len, wordDict))  # 用于限制下面 j 的循环次数
        words = set(wordDict)  # 便于快速判断 s[j:i] in words # 集合
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int) -> bool:
            if i == 0:  # 成功拆分！ # 先前左闭端点，此时已全部分割
                return True
            for j in range(i - 1, max(i - max_len - 1, -1), -1): # max是右开断点，不取
                if s[j:i] in words and dfs(j): # 满足条件则递降（注意这里的j左闭端点，i右开端点）
                    return True
            return False

        return dfs(len(s))

# 递推
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len, wordDict))  # 用于限制下面 j 的循环次数
        words = set(wordDict)  # 便于快速判断 s[j:i] in words

        n = len(s)
        f = [True] + [False] * n # 前i个字符能否被分割（索引i右开端点），索引0意味空集令其可以被分割
        for i in range(1, n + 1): # 从左往右，确定f[i]的值
            for j in range(i - 1, max(i - max_len - 1, -1), -1): # 从右往左，判断分割情况
                if f[j] and s[j:i] in words:
                    f[i] = True
                    break # 只要一种切割满足，则不必再遍历j
        return f[n]