import sys
from itertools import combinations
sys.stdin = open('input.txt')

def dfs(i,s):
    global re_min, n
    if s > re_min:
        return
    if i == n:
        if s < re_min:
            re_min = s

    for j in range(n):
        if visited[j] == 0:
            visited[j] = 1
            print(matrix[i][j])
            dfs(i+1, s+matrix[i][j])
            visited[j] = 0


for tc in range(1,int(input()) + 1):
    n = int(input())
    visited = [i for i in range(n)]
    matrix = [list(map(int,input().split())) for _ in range(n)]
    re = 0
    re_min = 99999999
    dfs(0,0)
    print('#{} {}'.format(tc,re_min))
