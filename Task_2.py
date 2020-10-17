class Reverse_iter:
    def __init__(self, spisok):
        max_num = len(spisok)
        self.i = max_num - 1
        self.n = 0
        
    def __iter__(self):
        pass

    def __next__(self):
        if self.i >= self.n:
            i = self.i
            self.i -= 1
            return spisok[i]
        else:
            raise StopIteration()


spisok = [1, 2, 3, 5]
x = Reverse_iter(spisok)
print(next(x))
