def solution(a, b):
    both = []
    
    for i in a:
        for j in range(len(b)):
            if b[j] != '*':
                if i == b[j]:
                    b[j] = '*'

    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] != '*':
                if a[i] > b[j]:
                    both.append(b[j])
                    if j+1 == len(b):
                        both.append(a[i])
                        a[i] = '!'
                    b[j] = '*'
                else:
                    both.append(a[i])
                    a[i] = '!'
                    break

    while '*' in b:
        b.remove('*')
    both.extend(b)

    while '!' in a:
        a.remove('!')
    both.extend(a)
    
    return both



                    
    
