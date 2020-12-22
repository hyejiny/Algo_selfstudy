import sys
sys.stdin = open('input.txt')

def arr(r,c):
    global re, n

    re += matrix[r][c]
    nr = r + 1
    for i in range(n):
        if i != c:
            arr(nr,i)


for tc in range(1, int(input()) + 1):
    n = int(input())

    matrix = [map(int, input().split()) for _ in range(n)]

    re = 0