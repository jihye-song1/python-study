def solution(list,limit):
    sort_array=[]
    sort_array=sorted(list)
    count=0
    sum=0

    print(sort_array)

    if sort_array[0] > limit:
        print("count is ",count)
    else:
        for i in range(0,len(sort_array)):
            sum=sort_array[i]+sum
            if sum < limit:
                count=count+1
        print("count is ",count)



    


solution([300,100,230,120,90,150,60],300)
solution([300,500,100,200,400],50)