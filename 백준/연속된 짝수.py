import sys
sys.stdin = open('input.txt')

s,n = map(int,input().split())

li = list(map(int,input().split()))

re = []
m_re = 0
st = 0
for idx,i in enumerate(li):
    if i % 2 != 0:
        re.append(idx)
print(re)
if len(re) <= n:
    m_re = s -len(re)
else:
    for i in range(n,len(re)):
        if re[i] - st - n > m_re:
            m_re = re[i] - st - n
            print(m_re)
        st = re[i-n] + 1

print(m_re)