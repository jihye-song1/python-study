# upper bound search  찾고자 하는 값보다 큰 것 중에서 가장 작은 값을 찾아주는 이분검색방법

def solution(nums, weight):
    left = 0 
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if weight >= nums[mid]:
            left = mid + 1
        else:
            right = mid

    return -1 if right == len(nums) else right


print(solution([100,120,150,160,165,170,175,180,190,200],175))
    
