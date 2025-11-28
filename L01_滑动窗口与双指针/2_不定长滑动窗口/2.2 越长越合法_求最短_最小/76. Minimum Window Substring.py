# 76. Minimum Window Substring

# 哈希+滑动窗口
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 哈希表：Counter()
        cnt_s=Counter()
        cnt_t=Counter(t)
        m=len(s)
        ans_left,ans_right=-1,m
        left=0
        for right,c in enumerate(s):
            cnt_s[c]+=1
            while cnt_s>=cnt_t: # Counter可以直接比较
                if right-left<ans_right-ans_left:
                    ans_left,ans_right=left,right
                cnt_s[s[left]]-=1
                left+=1
        return s[ans_left:ans_right+1] if ans_left!=-1 else "" # 如果ans_left更新过，则以ans为区间值
# 时间复杂度：O(|Sigma|*m+n)，|Sigma|是哈希表大小,m是s大小，n是t大小
# 空间复杂度：O(|Sigma|)

# 优化
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        ans_left,ans_right=-1,m
        left=0
        cnt=defaultdict(int)
        for c in t:
            cnt[c]+=1
        less=len(cnt) # 记录s和t的字符差别，节省时间的重点便在于此
        for right,c in enumerate(s):
            cnt[c]-=1
            if cnt[c]==0:
                less-=1
            while less==0:
                if right-left<ans_right-ans_left:
                    ans_left,ans_right=left,right
                x=s[left]
                if cnt[x]==0:
                    less+=1 # 除非cnt已经是0，否则less不变
                # 无论如何，下两者必须动
                cnt[x]+=1
                left+=1
        return s[ans_left:ans_right+1] if ans_left!=-1 else ""
# 时间复杂度：O(m+n+|Sigma|)
# 空间复杂度：O(|Sigma|)