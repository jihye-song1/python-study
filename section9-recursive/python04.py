# 픽셀 수 구하기
from collections import deque

dx = [ -1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

count = 0 

def DFS(x,y,board):
    global count
    count += 1
    board[x][y]=0

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board[nx][ny] == 1:
            DFS(nx, ny, board)

def solution(board):
    answer = []
    global count
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                DFS(i,j,board)
                answer.append(count)
                count = 0

    return answer

    

print(solution([[0,1,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,1,0],[0,0,1,1,0]]))