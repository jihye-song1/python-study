def solution(list):
    result=[]
    listlen=len(list)

#    중복 없애는 for문
    for value in list:
        if value not in result:
            result.append(value)

    count=len(list)/2   # 몇개까지 먹을 수 있는지 

    if count > len(result):
        print(len(result))
    else:
        print(count)

solution([2,1,1,3,2,3,1,2])
solution([1,3,5,7,2,3,7,5,3,2,5,7,9,12])
solution([5,5,5,5,5,5,5])
solution([12,23,11,3,5,23,23,23,23,23,23,23])
solution([100,200,300,400,500,600,700,800])


