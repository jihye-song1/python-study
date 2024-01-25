def solution(x,y,d,board):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    run_flagx=0
    run_flagy=0
    else_flagy=0
    else_flagx=0
    answer=0
    #board[x][y] = 2 # 청소한 칸은 2로 변경한다 

    while 1:
        print("ans1",board[x][y])
        if board[x][y] == 0:
            answer = answer+1
            board[x][y] = 2
            flag=0
            for i in range(len(dx)):
                if 0<=x+dx[i]<3:
                    run_flagx=1
                if 0<=y+dy[i]<3:
                    run_flagy=1
                if run_flagx==1 & run_flagy==1:
                    if board[x+dx[i]][y+dy[i]] == 0:
                    #print("test :",board[x+dx[i]][y+dy[i]])
                        flag=1  # 4개의 방면에 청소되지 않은 룸이 있을 때 
                        run_flagx=0
                        run_flagy=0
            if flag==0:
                if d==0: # 방향이 북쪽일 때 
                    if y+1 >= m:
                        print("no back")
                        break
                    else:
                        print("yes back")
                        y=y+1
        else:
            flag=0
            for k in range(len(dx)):
                if 0<=x+dx[k]<3:
                    else_flagx=1
                if 0<=y+dy[k]<3:
                    else_flagy=1
                if else_flagx==1 & else_flagy==1:
                    if board[x+dx[k]][y+dy[k]] == 0:
                        flag=1
                else_flagx=0
                else_flagy=0
            if flag==0:
                if d==0:
                    if y+1 >= m:
                        print("no back")
                        break
                    else:
                        print("yes back")
                        y=y+1

    return answer 



n, m = map(int, input().split())
r,c,d=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
print(solution(r,c,d,arr))