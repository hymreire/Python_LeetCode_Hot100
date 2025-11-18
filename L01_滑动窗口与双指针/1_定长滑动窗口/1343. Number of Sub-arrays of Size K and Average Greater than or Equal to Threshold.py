# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        ans=0
        tmp=0
        for right,x in enumerate(arr):
            tmp+=x
            if right-left<k-1:
                continue
            if tmp/k>=threshold:
                ans+=1
            tmp-=arr[left]
            left+=1
        return ans

# 时间复杂度：O(n)、空间复杂度O(1)