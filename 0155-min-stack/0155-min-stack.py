class MinStack(object):

    def __init__(self):
        self.arr = []
        self.arr_min = []
        self.min = float('inf')

    def push(self, value):
        if self.min >= value :
            self.arr_min.append(value)
            self.min = value
        self.arr.append(value)

    def pop(self):
        dd = self.arr.pop()
        if self.min == dd :
            self.arr_min.pop()
            if self.arr_min :
                self.min = self.arr_min[-1]
            else :
                self.min = float("inf")
        
    def top(self):
        if self.arr :
            return self.arr[-1]
        
    def getMin(self):
        if self.arr_min :
            return self.arr_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()