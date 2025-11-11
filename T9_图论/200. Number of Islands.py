# 200. Number of Islands

# DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(i,j): # 扩散标记
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
                return
            grid[i][j]='2'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    ans+=1
        return ans