# 84. Largest Rectangle in Histogram

# 单调栈
# 三个写法的时间复杂度都一样，空间复杂度方法三最佳
# 方法三最好背，可以背方法三

# 三次遍历
# 单调栈的构造方法，类似每日温度那道题，分别采用从左往右和从右往左的方案
# 栈单调递增
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n # 左索引，存储左侧第一个小于当前高度的索引值 # -1表示左侧没有小于当前高度的值，因此都可以组成面积
        st = [] # 初始化栈
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h: # 比他大的值都被弹出去了
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)

        right = [n] * n # 右索引 # n表示右侧没有小于当前高度的值，因此都可以组成面积
        st.clear() # 清空栈，后面继续用
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while st and heights[st[-1]] >= h:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        ans = 0 # 初始化最大矩形面积
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1)) # 从左往右依次遍历，如果都可以组成面积，该公式仍然符合
        return ans

# 两次遍历：将先前分别计算left和right改为一起计算
# 栈单调递增：大于当前值的都弹出去了
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        st = []
        # 从左到右，
        # 例子：heights = [2,1,5,6,2,3]
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                right[st.pop()] = i # 第一个小于等于弹出值的就是当前索引 # 相等没关系，利用left总会遍历到最大值
            if st:
                left[i] = st[-1] # 第一个小于当前值的索引值
            st.append(i) # 栈单调递增

        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1)) # r虽然不准确，但是利用准确的left总会遍历到最大值
        return ans

# 一次遍历
# 栈单调递增
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)  # 最后大火收汁，用 -1 把栈清空
        st = [-1]  # 在栈中只有一个数的时候，栈顶的「下面那个数」是 -1，对应 left[i] = -1 的情况
        ans = 0
        # [2,1,5,6,2,3]
        for right, h in enumerate(heights):
            while len(st) > 1 and heights[st[-1]] >= h: # 直到找到小于等于栈顶的值时弹出索引
                i = st.pop()  # 矩形的高（的下标）
                left = st[-1]  # 栈顶下面那个数就是 left
                ans = max(ans, heights[i] * (right - left - 1)) # 计算面积的公式
            st.append(right)
        return ans