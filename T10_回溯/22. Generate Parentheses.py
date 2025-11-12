# 22. Generate Parentheses

# 选与不选
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        path=['']*(2*n)
        def dfs(l,r):
            if r==n:
                ans.append(''.join(path))
                return
            if l<n:
                path[l+r]='('
                dfs(l+1,r)
            if r<l:
                path[l+r]=')'
                dfs(l,r+1)
        dfs(0,0)
        return ans

# 枚举位置
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        path=[]
        def dfs(l,b):
            if len(path)==n:
                s=[')']*(2*n)
                for i in path:
                    s[i]='('
                ans.append(''.join(s))
                return
            for r in range(b+1):
                path.append(l+r) # 其实就是在l索引开始填r个右括号，然后再填一个左括号
                dfs(l+r+1,b-r+1)
                path.pop()
        dfs(0,0)
        return ans