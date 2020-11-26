from itertools import combinations

def solution(num_buns, num_required):
    keys = [[] for num in range(num_buns)]
    copies = num_buns - num_required + 1
    for key, bunnies in enumerate(combinations(range(num_buns), copies)):
        for bunny in bunnies:
            keys[bunny].append(key)

    return keys
