# 39. Combination Sum

# 回溯
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        n=len(candidates)
        def dfs(i,left):
            if left==0:
                ans.append(path.copy())
                return
            if i==n or left<0:
                return
            dfs(i+1,left) # 不选
            path.append(candidates[i])
            dfs(i,left-candidates[i]) # 选
            path.pop() # 撤销
        dfs(0,target)
        return ans

# 剪枝
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        n=len(candidates)
        candidates.sort()
        def dfs(i,left):
            if left==0:
                ans.append(path.copy())
                return
            if i==n or left<candidates[i]: # 剪枝
                return
            dfs(i+1,left)
            path.append(candidates[i])
            dfs(i,left-candidates[i])
            path.pop()
        dfs(0,target)
        return ans

# 枚举
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[]
        candidates.sort()
        n=len(candidates)
        def dfs(i,left):
            if left==0:
                ans.append(path.copy())
                return
            for j in range(i,n):
                if left<candidates[j]:
                    break
                path.append(candidates[j])
                dfs(j,left-candidates[j])
                path.pop()
        dfs(0,target)
        return ans

# 完全背包，动态规划
# 比较容易混淆的是f的索引和candidates的索引，这两个需要认真区分
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        f=[[False]*(target+1) for _ in range(n+1)] # f(i,j)：前i个元素，能否凑出target
        f[0][0]=True # 前0个元素（空集）可以凑出0（空集就是都不选）
        for i,x in enumerate(candidates):
            for j in range(target+1):
                f[i+1][j]=f[i][j] or j>=x and f[i+1][j-x]
        ans=[]
        path=[]
        def dfs(i,left):
            if left==0:
                ans.append(path.copy())
                return
            if left<0 or f[i+1][left]==False: # 剪枝，0到i没法组成答案
                return
            dfs(i-1,left) # 不选
            path.append(candidates[i])
            dfs(i,left-candidates[i]) # 选
            path.pop()
        dfs(n-1,target) # 从索引n-1开始考虑
        return ans