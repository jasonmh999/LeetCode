"""
Time: O(1)
Space: O(capacity)
"""

from collections import OrderedDict

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.memo=OrderedDict()
       
        
        

    def get(self, key: int) -> int:
        memo=self.memo
        if key in memo:
            temp=memo.pop(key)
            memo[key]=temp
            return temp
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        memo=self.memo
        if key in memo:
            memo.pop(key)
        memo[key]=value
        #check capacity
        if len(memo)>self.capacity:
            k=next(iter(memo))
            memo.pop(k)
        #print(len(memo), self.capacity)
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)





"""

to pop first item of ordereddict
k = next(iter(d)) # k = 'a'
v = d.pop(k) # v = 1


**
delete and re-insert to preserve order of least recently used

"""


