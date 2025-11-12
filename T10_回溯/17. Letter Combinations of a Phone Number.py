# 17. Letter Combinations of a Phone Number

# 回溯：枚举
Mapping='','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        n=len(digits)
        path=['']*n
        def dfs(i):
            if i==n:
                ans.append(''.join(path))
                return
            for c in Mapping[int(digits[i])]:
                path[i]=c
                dfs(i+1)
        dfs(0)
        return ans