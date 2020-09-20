import random

def solution(x1, y1, x2, y2):
    if (abs(x2-x1) <= 1) and (abs(y2-y1) <= 1):
        answer = True
    else:
        answer = False
    return answer

