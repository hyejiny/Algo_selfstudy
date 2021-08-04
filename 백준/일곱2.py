import sys
sys.stdin = open('input.txt')

li = []

for _ in range(9):
    a = int(input())
    li.append(a)

k = sum(li)
for i in range(len(li)):
    for j in range(i,len(li)):
        if k - (li[i]+li[j]) == 100:
            li.sort()
            print(li)
            break
    break
