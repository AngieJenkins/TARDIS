def solution(arr):
    arr2 = []
    a = range(len(arr))
    n = 0
    m = -1

    if len(arr) % 2 == 0:
        rounds = len(arr)//2
    else:
        rounds = len(arr)//2 + 1
    print(rounds)
        
    for i in range(rounds):
        for i in a:
            if arr[n][i] != '*':
                arr2.append(arr[n][i])
                arr[n][i] = '*'
            
        for i in a:
            if arr[i][m] != '*':
                arr2.append(arr[i][m])
                arr[i][m] = '*'
            
        for i in a:
            if arr[m][len(a)-1-i] != '*':
                arr2.append(arr[m][len(a)-1-i])
                arr[m][len(a)-1-i] = '*'

        for i in a:
            if arr[len(a)-1-i][n] != '*':
                arr2.append(arr[len(a)-1-i][n])
                arr[len(a)-1-i][n] = '*'
        n += 1
        m -= 1    
    return arr2
