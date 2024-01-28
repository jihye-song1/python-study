def solution(list):
    result=[]
    min_result=[]
    first=0
    sort_aray=[]
    last=[]
    
    j=0

    sort_array=sorted(list)
    #print(sort_array)
    

    for i in range(0,len(list)-1): #길이가 4면 0 1 2 까지만 돌도록 -1 해주기
        min=sort_array[i+1]-sort_array[i]
        result.append(min)

    #print(result)

    min_result=sorted(result)
    first=min_result[0]

    for k in range(0,len(result)):
        if first == result[k]:
            last.append([])
            last[j].append(sort_array[k])
            last[j].append(sort_array[k+1])
            j=j+1

    
    print(last)


solution([3,8,1,5,12])
solution([2,1,3,5,4])
solution([5,10,15,20,25,11])
solution([2,4,3,1,5,7,8,12,13,15,23])

