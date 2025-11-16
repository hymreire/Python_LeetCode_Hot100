# W476_Q4

# 思路：改为求递增子序列个数的问题即可，但是看起来也不太容易就是
# 这道题难度比较高，属于前缀和的题型，可以稍微背一下，做不出来也没关系

# 没做出来
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pass

# 灵神解答
# 二分查找
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # 找递增段
        left = []  # 递增段的左端点
        s = [0]  # 递增子数组个数的前缀和
        start = 0
        for i, x in enumerate(nums):
            if i == n - 1 or x > nums[i + 1]: # 当前递增段结束，i是右闭端点
                # 找到了一个递增段 [start, i]
                left.append(start) # 递增段左端点
                m = i - start + 1 # 递增段长度
                # 长为 m 的子数组中有 m*(m+1)/2 个递增子数组
                # 计算 m*(m+1)/2 的前缀和
                s.append(s[-1] + m * (m + 1) // 2) # 递增子数组个数的前缀和
                start = i + 1  # 下一个递增段的左端点

        ans = []
        for l, r in queries:
            i = bisect_right(left, l)  # 左端点严格大于 l 的第一个区间
            j = bisect_right(left, r) - 1  # 包含 r 的最后一个区间

            # l 和 r 在同一个区间
            if i > j: # i>j说明l和r在同一个递增段
                m = r - l + 1
                ans.append(m * (m + 1) // 2)
                continue # 直接计算当前递增段的长度，跳过后续计算

            # l 和 r 在不同区间
            # 分成三段 [l, left[i]) + [left[i], left[j]) + [left[j], r]
            # 中间那段的子数组个数用前缀和计算
            m = left[i] - l
            m2 = r - left[j] + 1
            # 前面计算的是前缀和，因此这里可以分为三大段，分别计算，然后相加
            ans.append(m * (m + 1) // 2 + (s[j] - s[i]) + m2 * (m2 + 1) // 2) # 这里的分类讨论难度最高
        return ans

# 记录下一个递增段的左端点
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # 计算递增子数组个数的前缀和
        s = [0] * (n + 1) # s[i+1]=前缀和计算以i为右端点的递增子数组个数
        cnt = 0
        for i, x in enumerate(nums):
            if i > 0 and x < nums[i - 1]:
                cnt = 0
            cnt += 1 # 1+2+...+m，因此在新段内每多一个递增元素，就多一个递增子数组
            # 现在 cnt 表示以 i 为右端点的新增的递增子数组个数
            s[i + 1] = s[i] + cnt # s[i+1]=前缀和计算以i为右端点的递增子数组个数

        # nxt[i] 表示 i 右边下一个递增段的左端点，若不存在则为 n
        nxt = [0] * n
        nxt[-1] = n
        for i in range(n - 2, -1, -1):
            nxt[i] = nxt[i + 1] if nums[i] <= nums[i + 1] else i + 1

        ans = []
        for l, r in queries:
            l2 = nxt[l]
            if l2 > r:  # l 和 r 在同一个区间
                m = r - l + 1
                ans.append(m * (m + 1) // 2)
            else:  # l 和 r 在不同区间
                # 分成 [l, l2) + [l2, r]
                # 由于 [l2, r] 中的每个右端点对应的左端点都在 [l2, r] 内，所以可以用前缀和计算
                m = l2 - l
                ans.append(m * (m + 1) // 2 + s[r + 1] - s[l2])
        return ans