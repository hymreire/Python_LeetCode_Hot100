# 3090. Maximum Length Substring With Two Occurrences

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left=ans=0
        cnt=defaultdict(int)
        for right,enter in enumerate(s):
            cnt[enter]+=1
            while cnt[enter]>2:
                outer=s[left]
                cnt[outer]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
# 时间复杂度O(n)，最差空间复杂度O(n)