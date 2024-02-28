def solutions(nums,limit):
    length=len(nums)
    i=0
    k=length-1
    sum=0
    flag=0

    for j in range(0,limit):
        print("nums[i], nums[k], i, k",nums[i],nums[k],i,k)
        if nums[i] < nums[k]:
            sum=sum+nums[k]
            k=k-1  # 한 칸 앞으로
        elif nums[i] > nums[k]:
            sum=sum+nums[i]
            i=i+1
        else:
            backup_k=k
            backup_i=i
            while flag==0:
                flag=0
                if nums[backup_i+1] < nums[backup_k-1]:
                    flag=1
                    sum=sum+nums[k]
                    k=k-1
                    break
                elif nums[backup_i+1] > nums[backup_k-1]:
                    flag=1
                    sum=sum+nums[i]
                    i=i+1
                    break
                else:
                    backup_i=backup_i+1
                    backup_k=backup_k-1
                
                if backup_i == backup_k:
                    break
    print("sum is ",sum)

#solutions([2,3,7,1,2,1,5],4)
#solutions([1,2,3,5,6,7,1,3,9],5)  #26
#solutions([1,30,3,5,6,7],3)       #38
solutions([1,2,15,3,6,7,8,9],5)   #35
#solutions([12,5,6,12,34,35,13,3,7,8,9],7) #117