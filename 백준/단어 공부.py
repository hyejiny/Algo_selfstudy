import sys
sys.stdin = open('input.txt')

word = input()

ndict = {}

nword = list(word.upper())

for i in nword:
    ndict[i] = ndict.get(i,0) +1

m = 0
re = ''
u = 0

for a,b in ndict.items():

    if b > m:
        m = b
        re = a
    elif b == m:
        u = b

if u == m:
    print('?')
else:
    print(re)