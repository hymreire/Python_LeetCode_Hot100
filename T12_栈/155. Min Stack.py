# 155. Min Stack

# 由于Python的列表就有栈的功能，所以这题实现起来没有难度
# 唯一要注意的就是不要min整个列表，最小前缀方法能更好地记录最小值

class MinStack:

    def __init__(self):
        self.st=[(0,inf)] # 哨兵，无意义，用于循环计算最小前缀 # 第一个表示栈值，第二个表示最小前缀

    def push(self, val: int) -> None:
        self.st.append((val,min(self.st[-1][1],val))) # 当前值和最小前缀比较

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int: # 最后加进来的就是顶部，列表很好实现这个功能
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()