from functools import reduce
from operator import mul

def product(xs):
    return 0 if not len(xs) else reduce(mul, xs)

def solution(xs):
    negative = [f for f in xs if f < 0]

    if len(negative) % 2 and negative != xs:
        xs.remove(max(negative))
    
    return str(product([x for x in xs if x]))
