def solution(a, b):
    both = a[:]
    for one in b:
        if one not in a:
            both.append(one)
    both = sorted(both)       
    return both

print(solution([1, 4, 4, 7, 8], [2, 4, 5, 8]))
