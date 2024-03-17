def solution(n):
    if n==1 or n==2:
        return 1
    else:
        return (solution(n-1)+solution(n-2))
    

print(solution(5))



