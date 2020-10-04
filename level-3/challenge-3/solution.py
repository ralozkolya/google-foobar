from math import ceil, log

def solution(n):
    steps = 0
    base = int(n)

    while base > 1:
        if base % 2 == 0:
            base /= 2
        elif base == 3 or base % 4 == 1:
            base -= 1
        else:
            base += 1

        steps += 1

    return str(steps)
    

