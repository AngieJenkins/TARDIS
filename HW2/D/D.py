def solution(n,k):
    krug = list(range(1, n+1))
    el = -1
    while len(krug) != 1:
        k2 = k - len(krug)*(k // len(krug))
        if len(krug[(el+1):]) < k2:
            el = (k2-1) - len(krug[(el+1):])
        else:
            el += k2
        del krug[el]
        el -= 1

    return krug[0]


