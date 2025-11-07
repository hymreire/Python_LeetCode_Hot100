# 239. Sliding Window Maximum

# 方法：单调队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        ans=[0]*(n-k+1)
        q=deque()
        for i,x in enumerate(nums):
            # 右入
            while q and nums[q[-1]]<=x:
                q.pop()
            q.append(i)
            # 左出
            left=i-k+1
            if q[0]<left:
                q.popleft()
            # 赋值
            if left>=0:
                ans[left]=nums[q[0]]
        return ans