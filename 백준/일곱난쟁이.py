import sys
sys.stdin = open('input.txt')

li = []

for _ in range(9):
    a = int(input())
    li.append(a)

s = sum(li)


for i in range(9):
    b = li.pop(0)
    if s - b > 100:
        b2 = s - b - 100
        if b2 in li:
            li.remove(b2)
            break
        else:
            li.append(b)
    else:
        li.append(b)


li.sort()

for i in li:
    print(i)
