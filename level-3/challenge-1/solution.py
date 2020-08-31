def listXOR(n):
    values = [ n, 1, n + 1, 0 ]
    return values[n % 4]

def rangeXOR(start, end):
    return listXOR(start - 1) ^ listXOR(end)

def solution(first, length):

    result = 0

    for i in range(length):
        start = first + (length * i)
        end = start + length - i - 1
        result ^= rangeXOR(start, end)

    return result
