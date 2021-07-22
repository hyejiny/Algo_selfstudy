import sys
sys.stdin = open('input.txt')


for tc in range(int(input())):
    n,u = input().split()
    n = int(n)
    li = list(u)

    k = ''
    for i in li:
        k = k + i*n

    print(k)