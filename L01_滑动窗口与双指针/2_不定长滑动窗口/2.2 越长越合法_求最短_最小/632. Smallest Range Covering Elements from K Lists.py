# 632. Smallest Range Covering Elements from K Lists

# 方法一：最小堆
# 可以这样形象化理解该算法，先竖着求出第一列的区间，然后更新最小值对应的列表的指针
# 然后不断判断来更新区间
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 构建最小堆：堆中始终只含每个列表的一个值
        h=[(arr[0],i,0) for i,arr in enumerate(nums)] # (列0元素值、列表i、索引0)
        heapify(h) # 构建最小堆
        # 初始化答案
        ans_l=l=h[0][0] # 初始化列0的左端点和最小左端点
        ans_r=r=max(arr[0] for arr in nums) # 初始化列0的右端点和最小右端点
        while h[0][2]+1<len(nums[h[0][1]]): # 最后一个最小列表值的索引达到该列表长度时，结束更新
            value,i,j=h[0] # 取最小值
            x=nums[i][j+1] # 指针沿最小值所在列表更新
            heapreplace(h,(x,i,j+1)) # 弹出最小值，压入新值
            l=h[0][0] # 更新左端点
            r=max(r,x) # 更新右端点（更新左端点后右端点也要更新）
            if r-l<ans_r-ans_l: # 更小则更新
                ans_l,ans_r=l,r
        return [ans_l,ans_r]
# 时间复杂度：O(L*log(n))，L是while操作数（全部元素数）、log(n)是堆操作元素数
# 时间复杂度：O(n)【存储堆元素】

# 方法二：排序+滑动窗口
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pairs=sorted((x,i) for (i,arr) in enumerate(nums) for x in arr) # 升序列表，(元素值、列表编号)
        ans_l,ans_r=-inf,inf # 初始化左右端点
        empty=len(nums) # 列表数量【后面还能用来判断种类数量是否足够】
        cnt=[0]*empty # 统计每个列表编号出现的次数
        left=0 # 升序列表索引
        for r,i in pairs:
            if cnt[i]==0: # 如果入的时候还没有该种类，则empty-=1
                empty-=1
            cnt[i]+=1
            # 出
            while empty==0: # 种类达到要求【注意这里用while】
                l,j=pairs[left] # 取左端点值
                # 更新
                if r-l<ans_r-ans_l:
                    ans_l,ans_r=l,r
                cnt[j]-=1
                if cnt[j]==0: # 该种类以及被清空
                    empty+=1
                left+=1
        return [ans_l,ans_r]
# 时间复杂度：O(L*log(L))【归并排序可以做到O(L*log(n))
# 空间复杂度：O(L)