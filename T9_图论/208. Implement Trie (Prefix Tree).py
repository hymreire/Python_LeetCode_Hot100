# 208. Implement Trie (Prefix Tree)

# 多叉树
# 这题没背下来，后面有时间认认真看
# 但是灵神解法和图也没啥关系，充其量就是一个多叉树
class Node:
    __slots__='son','end'
    def __init__(self):
        self.son={} # 字典 # 这个cur.son直接理解成一个指针即可
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.son:
                cur.son[c]=Node()
            cur=cur.son[c] # 滑动指针
        cur.end=True # 末尾的son激活end值

    def find(self,word):
        cur=self.root
        for c in word:
            if c not in cur.son:
                return 0 # 不存在
            cur=cur.son[c] # 滑动指针
        return 2 if cur.end else 1 # 1表示前缀，2表示匹配（匹配同样满足前缀）

    def search(self, word: str) -> bool:
        return self.find(word)==2

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix)!=0