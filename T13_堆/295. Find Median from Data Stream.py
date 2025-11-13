# 295. Find Median from Data Stream

class MedianFinder:
    def __init__(self):
        self.left = []  # 入堆的元素取相反数，变成最大堆
        self.right = []  # 最小堆

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heappush(self.left, -heappushpop(self.right, num)) # heap直接将空列表转换为堆数据结构，heap[0]有意义为堆顶
        else:
            heappush(self.right, -heappushpop(self.left, -num))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (self.right[0] - self.left[0]) / 2