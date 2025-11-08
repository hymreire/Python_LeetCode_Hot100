# 48. Rotate Image

# 旋转=转置+反转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i): # 这里不能遍历到n否则白转置了
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()

# 同步转置和反转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i,row in enumerate(matrix):
            for j in range(i+1,n): # 唯一要注意的是，这里必须沿着上三角转置，而不是像先前那样沿着下三角转置
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            row.reverse()