# 207. Course Schedule

# 有向图+DFS判断成环

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses # 这步无所谓，我就是简化一下，可以直接用numcourses
        g=[[] for _ in range(n)]
        c=[0]*n
        for i,j in prerequisites:
            g[j].append(i) # j指向i
        def dfs(i): # 判断成环
            c[i]=1 # 表示正在dfs
            for j in g[i]:
                if c[j]==1 or (c[j]==0 and dfs(j)): # 如果指向的节点在遍历状态，或还未开始遍历的节点将来成环
                    return True # 成环判断
            c[i]=2 # 该节点不在环中
            return False # 该节点不会成环
        for i,x in enumerate(c):
            if x==0 and dfs(i)==True:
                return False # 成环则无法完成课程
        return True