def solutions(nums,k):
    sum=0
    list=[]

    # 0일때 / x는 0개 & y는 뒤에서 4개 
    # 1일때 / x는 1개 & y는 뒤에서 3개

    # 0 4
    # 1 3
    # 2 2
    # 3 1
    # 4 0
    leng=len(nums)-1
    print("leng is ",leng)
    for i in range(0,k):
        # i = 0
        for l in range(0,i):
            sum=sum+nums[l]
            print("l is ",l)
        for m in range(k-i,i,-1):
            sum=sum+nums[k]
            k=k-1
        list.append(sum)
    print("list is ",list)
    

        

            



solutions([2,3,7,1,2,1,5],4)
#solutions([1,2,3,5,6,7,1,3,9],5)  #26
#solutions([1,30,3,5,6,7],3)       #38
#solutions([1,2,15,3,6,7,8,9],5)   #35
#solutions([12,5,6,12,34,35,13,3,7,8,9],7) #117