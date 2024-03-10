# lower bound search 찾고자 하는 값보다 크거나 같은 것 중에서 가장 작은 값을 찾아주는 이분검색방법

def solution(nums,weight):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if weight > nums[mid]:
            left = mid + 1
        else:
            rigth = mid

    return -1 if right == len(nums) else right

