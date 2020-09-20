def solution(a, b):
    both = a[:]
    for one in b:
        if one not in a:
            both.append(one)
    both = sorted(both)       
    return both

