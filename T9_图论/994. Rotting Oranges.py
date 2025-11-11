# 994. Rotting Oranges

# BFS

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans=0 # 时间
        fresh=0 # 新鲜橘子数
        q=[] # 列表存腐烂橘子
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        while q and fresh:
            ans+=1
            tmp=q
            q=[]
            for i,j in tmp:
                for a,b in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                    if 0<=a<m and 0<=b<n and grid[a][b]==1:
                        fresh-=1
                        q.append((a,b))
                        grid[a][b]=2
        return ans if fresh==0 else -1