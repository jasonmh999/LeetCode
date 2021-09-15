class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.stack=[]
        

    def push(self, x: int) -> None:
        stack=self.stack
        if len(stack)<self.maxSize:
            stack.append(x)
        return

    def pop(self) ->int:
        stack=self.stack
        if not stack:
            return -1
        else:
            return stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.stack))):
            self.stack[i]+=val
        return


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)