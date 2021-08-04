import sys
sys.stdin = open('input.txt')

n = int(input())

matrix = []

for i in range(n):
    b = list(input())
    matrix.append(b)

def dfs(x,y):
    global k
    matrix[x][y] = cnt
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny = x+dx,y+dy
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == '1':
            matrix[nx][ny] = cnt
            k += 1
            dfs(nx,ny)


cnt = 1
k = 1
li = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1':
            cnt += 1
            dfs(i,j)
            li.append(k)
            k = 1

print(cnt -1)
li.sort()
for i in li:
    print(i)