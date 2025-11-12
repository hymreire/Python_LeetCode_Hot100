# 73. Set Matrix Zeroes

# 方法1：使用两个布尔数组记录行和列是否需要清零
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 确定行索引和列索引
        row=[0 in r for r in matrix]
        col=[0 in c for c in zip(*matrix)]
        for i,r in enumerate(matrix):
            for j,c in enumerate(r):
                if row[i] or col[j]:
                    matrix[i][j]=0

# 方法2：使用第一行和第一列来存储判断值（空间优化）
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        row0bool=0 in matrix[0]# 判断第一行是否有0
        col0bool=any(0==row[0] for row in matrix)# 判断第一列是否有0

        for i in range(1,m):
            for j in range(1,n):
                # 如果除开第一行第一列的矩阵元素为0，则用第一行第一列来存储判断值
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1,m):
            for j in range(1,n):
                # 如果第一行第一列存储的判断值为0，直接将这一行列全部归0
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        # 最后将第一行第一列按照先前的判断值来置0
        if row0bool:
            for j in range(n):
                matrix[0][j]=0

        if col0bool:
            for i in range(m):
                matrix[i][0]=0

## 灵神在这里给出了方法2的三种写法，但是我粗略扫了一遍，其实都是大同小异，只是写法不同而已
## 这里就暂时忽略另外两种写法，有空再做细致的分析吧：
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]

        for i in range(1, m):
            for j in range(n):  # 如果第一列包含 0，那么 matrix[0][0] 会置为 0
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 注意顺序，先改第一列，再改第一行（避免把 matrix[0][0] 从 1 改成 0 影响判断）
        if matrix[0][0] == 0:  # 替换原来的 first_col_has_zero
            for row in matrix:
                row[0] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            # 倒着遍历，避免提前把 matrix[i][0] 改成 0，误认为这一行要全部变成 0
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0