def solution(arr):
    n = 1
    m = 1
    maxi = 0
    if len(arr) == 1:
        maxi = 1
    else:
        while n < len(arr):
            if arr[n-1] == arr[n]:
                m += 1
            else:
                if m > maxi:
                    maxi = m
                m = 1
            n += 1
    return maxi

