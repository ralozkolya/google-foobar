from solution import solution

print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
print(solution([2,-3,1,0,-5]))
print(solution([2,-3,1,0,-1, -1]))
print(solution([1]))
print(solution([-1]))
print(solution([-1, 0]))

assert solution([2, 0, 2, 2, 0]) == '8'
assert solution([-2, -3, 4, -5]) == '60'
assert solution([2,-3,1,0,-5]) == '30'
