def solution(n):
    stepen = 1
    stroka = []
    while True:
        a = n - stepen
        if a >= 0:
            stroka.append(stepen)
            stepen = stepen *2
        else:
            break
    return stroka
