class MinStack:
    
    def __init__(self):
        self.minStack = []
        self.stackMin = []
    
    def push(self, val: int) -> None:
        if len(self.stackMin) > 0: 
            currMin = self.stackMin[-1]
            self.stackMin.append(min(val, currMin))
        else: 
            self.stackMin.append(val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stackMin.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
