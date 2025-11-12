# 131. Palindrome Partitioning

# 选与不选，确定切割的位置（两个dfs）
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        path=[]
        n=len(s)
        def dfs(i,st):
            if i==n:
                ans.append(path.copy())
                return
            if i<n-1: # i到n-1时必须切割，否则可以选择不切割
                dfs(i+1,st)
            t=s[st:i+1]
            if t==t[::-1]:
                path.append(t)
                dfs(i+1,i+1) # 从切割点后开始
                path.pop()
        dfs(0,0)
        return ans

# 枚举，结束位置（for循环）
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        path=[]
        n=len(s)
        def dfs(i):
            if i==n:
                ans.append(path.copy())
                return
            for j in range(i,n):
                t=s[i:j+1]
                if t==t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans