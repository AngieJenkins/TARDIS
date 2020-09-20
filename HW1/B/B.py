def solution(n):
    pinguin1 = '   _~_   '
    pinguin2 = '  (o o)  '
    pinguin3 = ' /  V  \ '
    pinguin4 = '/(  _  )\\'
    pinguin5 = '  ^^ ^^  '

    if n == 0:
        picture = ''
    else:
        picture = pinguin1*n + '\n' + pinguin2*n + '\n' + pinguin3*n + '\n' + pinguin4*n + '\n' + pinguin5*n
    return(picture)


