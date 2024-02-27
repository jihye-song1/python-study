def solution(list):
    list.sort(key = lambda v : (v[0],v[1]))
    print(list)


n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
solution(arr)