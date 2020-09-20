def solution(total):
    if total/60 > 24:
        total = total - 24*60*(total//60//24)
    hours = total//60
    minutes = total%60
    time = str(hours) + ' ' + str(minutes)
    return time 

