def solution(a, b):
    if b == 0:
        return a
    return 1 + solution(a, b-1)
