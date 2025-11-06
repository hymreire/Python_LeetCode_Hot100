# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list) # 可初始化列表的字典，功能更强
        for s in strs:
            d_sort="".join(sorted(s)) # sorted正排序
            d[d_sort].append(s)
        return list(d.values()) # values()导出defaultdict格式的键值