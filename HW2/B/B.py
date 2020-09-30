def solution(x):
    h = []
    for i in range(len(x)):
        if x[i] == 'h':
            h.append(i)

    s = list(x)
    for ind in h[1:-1]:
        s[ind] = 'H'    

    n = 1
    while n < len(s):
        if n % 3 == 0:
            s[n] = '*'
        n += 1

    x = "".join(s)
    x = x.replace('*', '').replace('1', 'one')
            
    return x
