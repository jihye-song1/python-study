def solution(member):
    member.sort(key = lambda v : (v[0],v[1]))

    for i in member:
        print(i[0],i[1])


n = int(input())
arr = []
for i in range(n):
    a, b = input().split()
    a = int(a)
    arr.append([a, b])
solution(arr)