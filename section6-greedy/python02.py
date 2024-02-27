def solution(list,limit):
    list.sort(key = lambda v : -v[1])  # 내림차순으로 주어진 배열 정렬



solution([[2,20],[2,10],[3,15],[2,30]],5)