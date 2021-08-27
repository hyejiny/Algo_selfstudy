import sys
sys.stdin = open('input.txt')

n = int(input())
li = list(map(int, input().split()))
cal = list(map(int,input().split()))
cal_max = 0
cal_min = 10000000000000000000


def dfs(x,s):
    global cal_max,cal_min
    if x == n-1:
        if s > cal_max:
            cal_max = s
        if s < cal_min:
            cal_min = s

    if cal[0] > 0:
        cal[0] -= 1
        dfs(x+1,s+li[x+1])
        cal[0] += 1

    if cal[1] > 0:
        cal[1] -= 1
        dfs(x+1,s-li[x+1])
        cal[1] += 1

    if cal[2] > 0:
        cal[2] -= 1
        dfs(x+1,s*li[x+1])
        cal[2] += 1

    if cal[3] > 0:
        cal[3] -= 1
        dfs(x+1,int(s/li[x+1]))
        cal[3] += 1

dfs(0,li[0])
print(cal_max)
print(cal_min)
