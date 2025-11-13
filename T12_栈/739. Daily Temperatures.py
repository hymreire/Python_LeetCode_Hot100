# 739. Daily Temperatures

# 从右往左
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n # 初始化答案
        st = [] # 候选大元素（栈）
        for i in range(n - 1, -1, -1): # 从右往左
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]: # 如果左边出现了比栈顶更大的元素，连续弹出栈顶
                st.pop()
            if st: # 如果栈中仍有元素，则计算栈顶和当前元素的差值
                ans[i] = st[-1] - i
            st.append(i) # 最右边的元素肯定得添加进来
        return ans

# 从左往右
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []  # 存储未计算出答案的索引
        for i, t in enumerate(temperatures):
            # 右边的值大于栈顶，弹出栈顶，计算差异
            # 这也说明栈顶一定是栈中最小的值
            while st and t > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j # 计算索引差
            st.append(i) # 先把索引0加入栈顶
        return ans