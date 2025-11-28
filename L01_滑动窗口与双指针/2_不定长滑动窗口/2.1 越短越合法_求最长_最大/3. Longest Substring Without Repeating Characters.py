# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        ans=0
        cnt=defaultdict(int)
        for right,c in enumerate(s):
            cnt[c]+=1
            while cnt[c]>1:
                cnt[s[left]]-=1 # 经典索引错误：cnt[left]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
# 时间复杂度：O(n)、最差的空间复杂度O(n)