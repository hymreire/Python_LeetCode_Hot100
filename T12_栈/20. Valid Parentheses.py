# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        mp={')':'(','}':'{',']':'['}
        st=[]
        for c in s:
            if c not in mp:
                st.append(c)
            elif not st or st.pop()!=mp[c]: # c不入栈时，栈空（避免pop报错）或无法匹配意味着非法
                return False
        return not st