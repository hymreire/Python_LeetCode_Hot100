# 74. Search a 2D Matrix

# 二分法：自己写
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        left,right=0,m*n-1
        while left<=right:
            mid=(left+right)//2
            i,j=mid//n,mid%n
            if matrix[i][j]<target:
                left=mid+1
            elif matrix[i][j]==target:
                return True
            else:
                right=mid-1
        return False

# 二分法：库函数
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        i=bisect_left(range(m*n),target,key=lambda i: matrix[i//n][i%n])
        return i<m*n and matrix[i//n][i%n]==target

# 排除法（时间复杂度高于二分法，在本题中）
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        i,j=0,n-1
        while i<m and j>=0:
            if matrix[i][j]<target:
                i+=1
            elif matrix[i][j]==target:
                return True
            else:
                j-=1
        return False