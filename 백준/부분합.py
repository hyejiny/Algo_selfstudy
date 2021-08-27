import sys
sys.stdin = open('input.txt')

n,s = map(int,input().split())

li = list(map(int,input().split()))

re = []
st = 0
e = 1

while True:
    if e == n:
        break

    elif sum(li[st:e+1]) < s:
        e += 1

    else:
        re.append(e-st+1)
        st += 1

print(min(re))


