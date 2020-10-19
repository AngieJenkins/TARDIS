class OneIndexedList:
    def __init__(self, items):
        self.items = items or []

    def __getitem__(self, idx):
        return self.items[idx-1]
        
    def __setitem__(self, idx, value):
        self.items[idx-1] = value
        

b = OneIndexedList([1,2,3])
print(b[1])
