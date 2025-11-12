# 51. N-Queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        queen=[0]*n # 存列号
        co=[False]*n # 列号
        d1=[False]*(2*n-1) # 行加列
        d2=[False]*(2*n-1) # 行减列
        def dfs(i):
            if i==n:
                ans.append(['.'*c+'Q'+'.'*(n-1-c) for c in queen])
                return
            for j in range(n): # 枚举列号
                if not co[j] and not d1[i+j] and not d2[i-j]: # 列号j
                    queen[i]=j
                    co[j]=d1[i+j]=d2[i-j]=True
                    dfs(i+1)
                    co[j]=d1[i+j]=d2[i-j]=False
        dfs(0)
        return ans