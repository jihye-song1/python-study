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
solution([300,100,230,120,90,150,60],700)
solution([50,90,70,120,300,200,150,180,190],1000)
solution([70,90,100,80,60,75,73,85,120,110,200],800)