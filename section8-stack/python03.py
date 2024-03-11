from collections import deque
def solution(nums):
    answer = 0
    leng=len(nums)
    array = deque()
    flag = 0 

    for x in range(0,leng):
       array.append(nums[x])

    #print("first array is ", array)
    
    while leng > 2:
        for _x in range(0,2):
            #print("value is ",array[0])
            array.popleft()
        leng = leng - 2
        
        for _x in range(0,1):
            #print("aaa is ",array[0])
            array.append(array[0])
            array.popleft()
        #leng = leng - 1
        #print("list is ", array)

        if leng == 2:
            flag = 1
            break
    if flag == 0:
        answer = array[0]
    else:
        answer = array[1]

    return answer
            
print(solution([3, 1, 4, 5, 2, 6, 7]))
print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))