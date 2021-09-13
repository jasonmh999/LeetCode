"""
Time: O(1)
Space: O(1)
"""

class RecentCounter:

    def __init__(self):
        self.queu=deque()
        

    def ping(self, t: int) -> int:
        self.queu.append(t)
        
        while self.queu[0] < t-3000:
            self.queu.popleft()
        
        return len(self.queu)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)