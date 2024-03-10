from bisect import bisect_left, bisect_right

def solution(nums, weight):
    answer = bisect_left(nums, weight)
    pay = answer * 10
    print("answer is ",answer)
    print("pay is ", pay)

    return -1 if answer == len(nums) else answer

print(solution([100,120,150,160,165,170,175,180,190,200], 170))
print(solution([200,250,260,265,275,290,300,325,350,370],270))
print(solution([20,30,40,50,60,70],90))