def solution(nums,target):
    left=0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            left  = mid + 1
        else:
            right = mid - 1
    return -1


print(solution([2,5,7,8,10,15,20,24,25,30],8))  
print(solution([-3,0,2,5,8,9,12,15],0))