# 1358. Number of Substrings Containing All Three Characters

# 依旧固定右端点
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans=0
        left=0
        cnt=defaultdict(int)
        for right,c in enumerate(s):
            cnt[c]+=1
            while len(cnt)==3: # 一直到left不满足条件使结束
                outer=s[left]
                cnt[outer]-=1
                if cnt[outer]==0:
                    del cnt[outer]
                left+=1
            ans+=left # 先前left=0
        return ans
# 时间复杂度：O(n|Sigma|)
# 空间复杂度：O(|Sigma|)
# |Sigma|是哈希表大小