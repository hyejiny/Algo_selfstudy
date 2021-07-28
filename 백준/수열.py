import sys
sys.stdin = open('input.txt')

n,k = map(int,input().split())

li = list(map(int,input().split()))

re = sum(li[:k])
m_re = re


for i in range(k,n):
    re += li[i] - li[i-k]
    if re > m_re:
        m_re = re


print(m_re)



# n,k = map(int,input().split())
#
# li = list(map(int,input().split()))
#
# m = 0
# for i in range(n-k):
#     if sum(li[i:i+k]) > m:
#         m = sum(li[i:i+k])
#
# print(m)