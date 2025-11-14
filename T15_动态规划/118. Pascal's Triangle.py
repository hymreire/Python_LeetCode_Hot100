# 118. Pascal's Triangle

# 递推
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = [[1] * (i + 1) for i in range(numRows)] # 全1初始化
        for i in range(2, numRows):  # 行从索引2开始计算直到最后一行
            for j in range(1, i): # 列从索引1开始直到倒数第二列（第i行有i+1个元素，倒数第二列的右开区间是i）
                # 左上方的数 + 正上方的数
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
        return c