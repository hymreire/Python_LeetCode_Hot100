# 240. Search a 2D Matrix II

# 排除法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        i,j=0,n-1
        while i<m and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return False