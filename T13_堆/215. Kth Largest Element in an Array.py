# 215. Kth Largest Element in an Array

# 快速排序：二分法【这题不能用堆排序，不满足时间复杂度】
# 推导不容易，但是答案还是比较好背
class Solution:
    def quicksort(self,nums,left,right):
        i=randint(left,right)
        pivot=nums[i]
        nums[left],nums[i]=nums[i],nums[left]
        i,j=left+1,right
        while True:
            while i<=j and nums[i]<pivot: # 保证i值大于等于pivot（左边全部小于等于，等于在后面体现）
                i+=1
            while i<=j and nums[j]>pivot: # 保证j值小于等于pivot（右边全部大于等于，等于在后面体现）
                j-=1
            if i>=j:
                break
            nums[i],nums[j]=nums[j],nums[i] # 将不满足要求的值交换
            i+=1
            j-=1
        nums[j],nums[left]=nums[left],nums[j]
        return j
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left,right=0,n-1
        while True:
            index=self.quicksort(nums,left,right)
            if index==n-k:
                return nums[index]
            elif index<n-k:
                left=index+1
            else:
                right=index-1

# 灵神带注解的答案，值得品读
class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        """
        在子数组 [left, right] 中随机选择一个基准元素 pivot
        根据 pivot 重新排列子数组 [left, right]
        重新排列后，<= pivot 的元素都在 pivot 的左侧，>= pivot 的元素都在 pivot 的右侧
        返回 pivot 在重新排列后的 nums 中的下标
        特别地，如果子数组的所有元素都等于 pivot，我们会返回子数组的中心下标，避免退化
        """

        # 1. 在子数组 [left, right] 中随机选择一个基准元素 pivot
        i = randint(left, right)
        pivot = nums[i]
        # 把 pivot 与子数组第一个元素交换，避免 pivot 干扰后续划分，从而简化实现逻辑
        nums[i], nums[left] = nums[left], nums[i]

        # 2. 相向双指针遍历子数组 [left + 1, right]
        # 循环不变量：在循环过程中，子数组的数据分布始终如下图
        # [ pivot | <=pivot | 尚未遍历 | >=pivot ]
        #   ^                 ^     ^         ^
        #   left              i     j         right

        i, j = left + 1, right
        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            # 此时 nums[i] >= pivot

            while i <= j and nums[j] > pivot:
                j -= 1
            # 此时 nums[j] <= pivot

            if i >= j:
                break

            # 维持循环不变量
            nums[i], nums[j] = nums[j], nums[i] # 交换，避免卡住，小于等于、大于等于满足前面的假设
            i += 1
            j -= 1

        # 循环结束后
        # [ pivot | <=pivot | >=pivot ]
        #   ^             ^   ^     ^
        #   left          j   i     right

        # 3. 把 pivot 与 nums[j] 交换，完成划分（partition）
        # 为什么与 j 交换？
        # 如果与 i 交换，可能会出现 i = right + 1 的情况，已经下标越界了，无法交换
        # 另一个原因是如果 nums[i] > pivot，交换会导致一个大于 pivot 的数出现在子数组最左边，不是有效划分
        # 与 j 交换，即使 j = left，交换也不会出错
        nums[left], nums[j] = nums[j], nums[left]

        # 交换后
        # [ <=pivot | pivot | >=pivot ]
        #               ^
        #               j

        # 返回 pivot 的下标
        return j

    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        target_index = n - k  # 第 k 大元素在升序数组中的下标是 n - k
        left, right = 0, n - 1  # 闭区间
        while True:
            i = self.partition(nums, left, right)
            if i == target_index:
                # 找到第 k 大元素
                return nums[i]
            if i > target_index:
                # 第 k 大元素在 [left, i - 1] 中
                right = i - 1
            else:
                # 第 k 大元素在 [i + 1, right] 中
                left = i + 1