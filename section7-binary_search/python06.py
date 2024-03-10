def solution(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
         
        if nums[mid] == mid:
            return nums[mid]
        
        if nums[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(solution([-3,-2,0,1,3,5,8,9,12]))