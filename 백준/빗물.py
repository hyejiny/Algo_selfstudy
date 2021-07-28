import sys
sys.stdin = open('input.txt')

h,w = map(int, input().split())

li = list(map(int,input().split()))

re = 0

for i in range(len(li)):
    left_top = max(li[:i+1])
    right_top = max(li[i:])
    k = min(left_top,right_top)

    re += k - li[i]

print(re)

