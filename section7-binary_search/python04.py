from bisect import bisect_left, bisect_right

def solution(nums, weight):
    answer = bisect_left(nums, weight)
    answer_right = bisect_right(nums,weight)
    print("answer is ",answer)
    print("upper bound is ",answer_right)
    return answer


print(solution([70,80,80,80,80,90,90,90],90))