def memoize(func):
    cache = {}
    def handler(remaining, current):
        if remaining not in cache:
            cache[remaining] = {}
        if current not in cache[remaining]:
            cache[remaining][current] = func(remaining, current)
        return cache[remaining][current]
    return handler

@memoize
def stairs_number(remaining, current):

    if remaining == 0:
        return 1

    if remaining < 0:
        return 0

    return (stairs_number(remaining - 1, current + 1)
        + stairs_number(remaining - current - 1, current + 1))

def solution(n):
    return stairs_number(n - 1, 1) - 1
