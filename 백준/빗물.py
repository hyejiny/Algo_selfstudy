import sys
sys.stdin = open('input.txt')

h,w = map(int, input().split())

li = list(map(int,input().split()))


k = 0
for i in range(0,len(li)-1):
    if li[i+1] < li[i]:
