# 54. Spiral Matrix

# 方法一：标记+模拟方向
Direction=(0,1),(1,0),(0,-1),(-1,0)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        m,n=len(matrix),len(matrix[0])
        di=0
        i,j=0,0
        for _ in range(m*n):
            ans.append(matrix[i][j])
            matrix[i][j]=None
            x,y=i+Direction[di][0],j+Direction[di][1]
            if x<0 or x>=m or y<0 or y>=n or matrix[x][y]==None:
                di=(di+1)%4
            i,j=i+Direction[di][0],j+Direction[di][1]
        return ans

# 方法二：优化，去除矩阵标记，直接修改矩阵
Direct=(0,1),(1,0),(0,-1),(-1,0)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        m,n=len(matrix),len(matrix[0])
        size=m*n
        i,j,di=0,-1,0
        while len(ans)<size:
            for _ in range(n):
                i,j=i+Direct[di][0],j+Direct[di][1]
                ans.append(matrix[i][j])
            di=(di+1)%4
            n,m=m-1,n # 亮点
        return ans