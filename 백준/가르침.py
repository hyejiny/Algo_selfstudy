import sys
sys.stdin = open('input.txt')

n,k = map(int, input().split())
max_re = 0
re = ['a','n','t','i','c']
re2 = {}

if k < 5 :
    max_re = 0
else:
    for i in range(n):
        li = set(input())
        for j in li:
            if j not in re:
                re2[j] = re2.get(j,0) +1
nre = sorted(re2.items(),key=lambda x:x[1],reverse=True)
print(re2)
if k >= len(re2) + 5:
    max_re = n
else:
    m = k - len(re2)
    print(m)
    for i in range(0,m):
        print(nre[i])
# print(max_re)






