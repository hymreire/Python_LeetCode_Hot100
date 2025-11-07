# 3. Longest Substring Without Repeating Characters

# 写法1：哈希表（整型数组）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt=defaultdict(int)
        left=0
        ans=0
        for right,c in enumerate(s):
            cnt[c]+=1 # int默认字典值为0
            while cnt[c]>1:
                cnt[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans

# 写法2：哈希集合（布尔数组）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=ans=0
        window=set()
        for right,c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left+=1
            window.add(c)
            ans=max(ans,right-left+1)
        return ans