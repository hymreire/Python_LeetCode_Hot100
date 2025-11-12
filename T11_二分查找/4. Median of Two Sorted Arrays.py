# 4. Median of Two Sorted Arrays

# 二分法保证算法的时空复杂度最优，但是这题很难背，以后有机会再做详细地分析
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a)>len(b):
            a,b=b,a # 确保二分搜索的时间最优
        m,n=len(a),len(b)
        # 闭区间写法
        left,right=0,m-1
        while left<=right:
            i=(left+right)//2
            j=(m+n-3)//2-i
            if a[i]<b[j+1]: # 这样写更快，但其实改成小于等于也能过
                left=i+1
            else:
                right=i-1
        i=left-1
        j=(m+n-3)//2-i
        # 安全地获取左半和右半
        ai=a[i] if i>=0 else -inf
        bj=b[j] if j>=0 else -inf
        ai1=a[i+1] if i+1<m else inf
        bj1=b[j+1] if j+1<n else inf
        max1=max(ai,bj)
        min2=min(ai1,bj1)
        # 最后计算中位数
        return max1 if (m+n)%2 else (max1+min2)/2