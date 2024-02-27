def solution(m,nums):
    answer=0
    n=len(nums)

    nums.sort(key = lambda v : v[0])

    start = end = i = 0 

    while i < n:
        while i < n and nums[i][0] <= start:
            end = max(end, nums[i][1])
            i += 1
        answer += 1
        if end == m:
            return answer
        start = end

    return answer


print(solution(12,[[5,10],[1,8],[0,2],[0,3],[2,5],[2,6],[10,12],[7,12]]))