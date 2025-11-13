# 394. Decode String


# 三种方法时空复杂度一样，建议背方法一，如有必要可以看一下方法三，方法二没必要背

# 递归
class Solution:
    def decodeString(self, s: str) -> str:
        if not s: # 返回空串（边界条件）
            return s
        if s[0].isalpha(): # 单字母直接返回即可
            return s[0]+self.decodeString(s[1:])
        # 非字母（其实就是数字）
        i=s.find("[") # 找左括号的索引，因为数字最大可达300
        balance=1 # balance用来权衡左右括号的数量差异（就是括号匹配问题）
        for j in count(i+1): # 类似于while和for的组合体，从i+1开始逐渐增加，直到终止
            if s[j]=='[':
                balance+=1
            if s[j]==']':
                balance-=1
            if balance==0: # 终止条件
                return self.decodeString(s[i+1:j])*int(s[:i])+self.decodeString(s[j+1:])

# 另一种递归方案，感觉没有很大的差异，就不自己写一遍了
# 这里要判断的细节很多，时空复杂度和上面一样，建议采用上面那种方法
class Solution:
    def decodeString(self, s: str) -> str:
        i = 0 # 全局指针i
        def decode() -> str:
            nonlocal i
            res = ''
            k = 0 # 每个递归重置自己的k
            while i < len(s): #  全局边界条件
                c = s[i]
                i += 1
                if c.isalpha(): # 字母直接加到res上
                    res += c
                elif c.isdigit(): # 数字则更新计数，比如231=2*10*10+3*10+1
                    k = k * 10 + int(c)
                elif c == '[':  # 遇到左括号则递降
                    res += decode() * k  # 把括号内的字符串重复 k 次
                    k = 0  # 重置 k，若不重置，2[a]3[b] 后面的 3 会算出 k = 23
                else:  # ']' 归
                    break
            return res
        return decode()

# 用栈模拟递归
# 是方法二的手动栈实现（递归本质是栈）
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # 用于模拟计算机的递归
        res = ''
        k = 0
        for c in s:
            if c.isalpha():
                res += c
            elif c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                # 模拟递归
                # 在递归之前，把当前递归函数中的局部变量 res 和 k 保存到栈中
                stack.append((res, k))
                # 递归，初始化 res 和 k
                res = ''
                k = 0
            else:  # ']'
                # 递归结束，从栈中恢复递归之前保存的局部变量
                pre_res, pre_k = stack.pop()
                # 此时 res 是下层递归的返回值，将其重复 pre_k 次，拼接到递归前的 pre_res 之后
                res = pre_res + res * pre_k
        return res