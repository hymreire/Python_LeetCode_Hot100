# 3325. Count Substrings With K-Frequency Characters I

# 单指针，滑动窗口
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans=left=0
        cnt=defaultdict(int)
        for c in s:
            cnt[c]+=1
            while cnt[c]>=k:
                outer=s[left]
                cnt[outer]-=1
                left+=1
            ans+=left
        return ans
# 时间复杂度：O(n+|Sigma|)，|Sigma|是字符集大小
# 空间复杂度：O(|Sigma|)