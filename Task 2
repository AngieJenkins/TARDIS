from collections import deque 

class MinStack(object):

    def __init__(self):
        self.d = deque()
        self.min = deque()
    

    def push(self, x):
        self.d.append(x)
        
        if not self.min:
            self.min.append(x)
        else:
            if self.min[-1] >= x:
                self.min.append(x)

    def pop(self):
        el = self.d.pop()
        
        if el == self.min[-1]:
            self.min.pop()
        

    def top(self):
        return self.d[-1]
        

    def getMin(self):
        return self.min[-1]
