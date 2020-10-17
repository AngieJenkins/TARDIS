def integers():
    i = 0
    for i in range(1, 5):
#    while True:
        yield i
        i += 1

def squares():
    for number in integers():
        yield number ** 2

def take(n, generator):
    numbers = []
    j = 0
    a = generator
    
    try:
        while j < n:
            numbers.append(next(a))
            j += 1
        return(numbers)

    except(StopIteration):
        for i in a:
            numbers.append(i)
        return(numbers)

n = 5
generator = squares()
print(take(n, generator))

