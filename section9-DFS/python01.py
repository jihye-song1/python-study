def solution(n):
    if n==1:
        return 1
    else:
        return n*solution(n-1)
    

print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
