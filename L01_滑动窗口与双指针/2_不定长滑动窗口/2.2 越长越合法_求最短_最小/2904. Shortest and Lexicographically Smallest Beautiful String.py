# 2904. Shortest and Lexicographically Smallest Beautiful String

# 字符串，内建函数，count：https://www.runoob.com/python/att-string-count.html
# 字符串，比较运算符：https://juejin.cn/post/7132453491791888398
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1")<k:
            return ""
        ans=s # 初始化答案
        left=rec=0
        for right,c in enumerate(s):
            rec+=int(c)
            if rec<k:
                continue
            # 两种情况更新：1过多或者0在前
            while rec>k or s[left]=="0":
                rec-=int(s[left])
                left+=1
            if rec==k:
                t=s[left:right+1]
                # 两种情况更新：t更短或者t的字典序更小
                if len(t)<len(ans) or (len(t)==len(ans) and t<ans): # 字符串直接比较就是字典序
                    ans=t
        return ans
# 时间复杂度：O(n^2)：外层循环x内层比较字符串
# 空间复杂度：O(n)或O(1)：取决于是否考虑切片存储

# 用字符串哈希或后缀数组，将比较字符串的时间复杂度下降到O(log(n))，整体时间复杂度即为O(n*log(n))
