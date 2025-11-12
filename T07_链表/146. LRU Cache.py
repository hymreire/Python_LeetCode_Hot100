# 146. LRU Cache

# 方法：Collections库
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key,last=False)
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        self.cache[key]=value
        self.cache.move_to_end(key,last=False)
        if len(self.cache)>self.capacity:
            self.cache.popitem()

# 自己写一个库函数也可以，就是会比较耗时间
# 我这里放一个注释过的代码，但是我自己没背过，以后有时间再背一下
# 里面每一个函数都可以作为一道单独的题
# 这题是很典型的链表学习题
class Node:
    __slots__='prev','next','key','value' # 这个类只能有这四个属性
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        # 初始化哨兵节点
        self.dummy=Node()
        self.dummy.prev=self.dummy
        self.dummy.next=self.dummy
        self.key_to_node={}
    
    # 获取节点，链表置顶
    def get_node(self,key):
        if key not in self.key_to_node:
            return None
        node=self.key_to_node[key]
        # 置顶链表=移除+置顶
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key: int) -> int:
        node=self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node=self.get_node(key)
        if node:
            node.value=value
            return
        self.key_to_node[key]=node=Node(key,value)
        self.push_front(node)
        if len(self.key_to_node)>self.capacity:
            back_node=self.dummy.prev # 双向链表（环）
            del self.key_to_node[back_node.key] # 先在Hash表中删除
            self.remove(back_node) # 后在链表中删除
    
    def remove(self,x): # 双向链表（环）删除的经典操作：前后后前
        x.prev.next=x.next
        x.next.prev=x.prev

    def push_front(self,x): # 置顶需要成为dummy的下家
        x.prev=self.dummy
        x.next=self.dummy.next
        x.prev.next=x
        x.next.prev=x