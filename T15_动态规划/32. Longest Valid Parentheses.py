# 32. Longest Valid Parentheses

# 这题灵神没有解答，我用AI翻译一下
# 暂时先不背，后面再背

# 动态规划
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0 # 记录最大长度
        dp = [0] * len(s) # 记录以i结尾的最长有效括号长度
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # 如果前一个字符是左括号，则dp[i] = dp[i - 2] + 2（注意这里i>=2）
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(': # 如果前一个字符是右括号
                    # 情况：嵌套匹配，例如 s = "()(())"，当 i=5 时
                    # s[5]=')'，s[4]=')'，dp[4]=2（表示s[3]和s[4]匹配）
                    # 需要检查 s[5-dp[4]-1] = s[2] 是否为 '('
                    # 如果是，则 s[2] 和 s[5] 匹配，形成 "(()())"
                    # dp[i] = dp[i-1]（内部已匹配的长度）+ dp[i-dp[i-1]-2]（前面可能还有匹配的）+ 2（当前匹配的一对）
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0) + 2
                maxans = max(maxans, dp[i]) # 更新最大长度
        return maxans

# 栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]  # 初始化为 -1，作为边界标记
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i) # 遇到左括号则入栈
            else:
                stack.pop() # 遇到右括号则出栈
                if not stack:  # 栈为空，说明当前 ')' 没有匹配的 '('
                    stack.append(i)  # 更新边界
                else:
                    maxans = max(maxans, i - stack[-1]) # 更新最大长度 # 很巧妙的表达式
        return maxans # 返回最大长度

# 双指针（空间优化 O(1)）
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = maxlength = 0
        # 从左到右扫描
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
        
        left = right = 0
        # 从右到左扫描
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif left > right:
                left = right = 0
        
        return maxlength