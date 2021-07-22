import sys
sys.stdin = open('input.txt')

li = [0]*10

m = 1

for _ in range(3):
    a = int(input())
    m = m*a

n = str(m)

for i in n:
    k = int(i)
    li[k] += 1

for i in li:
    print(i)

