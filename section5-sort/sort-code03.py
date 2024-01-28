def solution(list,target):
    result=[]
    sort_array=[]
    plus=0
    flag=0

    sort_array=sorted(list)
    #print(sort_array)

    for i in range(0,len(list)-1):
        for k in range(i+1,len(list)):
            plus=sort_array[i]+sort_array[k]
            if plus == target:
                result.append(sort_array[i])
                result.append(sort_array[k])
                flag=1
                break

    if flag == 1 :
        print(result)
    else:
        print("[0, 0]")



solution([7,3,2,13,9,15,8,11],12)
solution([21,12,30,15,6,2,9,19,14],24)
solution([7,5,12,20],15)
