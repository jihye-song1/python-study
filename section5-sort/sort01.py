# sort => sort하는 인자들의 값을 sort한 상태로 바꿔버림

nums=[1,2,8,9,10,0,1,103,98]
nums.sort()
print(nums)

nums=[1,2,8,9,10,0,1,103,98]
nums.sort(reverse=True)
print(nums)

nums=[[1,2],[2,3],[1,3]]
nums.sort(key = lambda v : (v[1]))
print(nums)

nums=[[1,2],[2,3],[1,3]]
nums.sort(key = lambda v : (-v[1]))
print(nums)

nums=[[1,2],[2,3],[1,3]]
nums.sort(key = lambda v : (v[1],v[0]))
print(nums)


study=['d','s','t','u','y']
print(sorted('study'))
print(','.join(sorted('study')))
#join문 '구분자'.join(리스트)