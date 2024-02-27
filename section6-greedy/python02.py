def solution(list,limit):
    list.sort(key = lambda v : -v[1])  # 내림차순으로 주어진 배열 정렬
    sum=0
    count=0
    flag=0

    for i in range(0,len(list)):
        k=list[i][0]
        if flag==1:
            break
        for j in range(0,k): # 2 2 3 2
            count=count+1
            if count == limit:
                flag=1
                sum=sum+list[i][1]
                break
            sum=sum+list[i][1]
            
    print("sum is ",sum)
    print("count is ",count)



solution([[2,20],[2,10],[3,15],[2,30]],5)