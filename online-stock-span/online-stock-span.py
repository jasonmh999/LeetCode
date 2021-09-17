class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        counter=1
        
        stack=self.stack
        
        while stack and stack[-1][0]<=price:
            prev_price,prev_counter=stack.pop()
            counter+=prev_counter
            
            
        stack.append((price,counter))
        
        return counter
            
        
        
        """     
        counter=1
        for prev_item in reversed(self.stack):
            if price>=prev_item:
                counter+=1
            else:
                break            
            
        self.stack.append(price)
        return counter
    """
"""
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
"""
