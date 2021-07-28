import sys
sys.stdin = open('input.txt')


H, W = map(int, input().split())
block = list(map(int, input().split()))
stack = []
answer = 0
for i in range(W):
    # 스택이 비어있지 않고 (이전 높이들이 존재함)
    # 현재 높이가 이전 높이보다 크다면 (변곡점, 기준이 됨)
    while stack and block[i] > block[stack[-1]]:
        # 이전 블록의 인덱스를 top에 저장
        top = stack.pop()

        # 꺼냈을 때 스택이 빈다면 물이 찰 수가 없음
        if not stack:
            break

        # 거리구하기
        distance = (i - stack[-1]) - 1
        # 높이구하기
        height = min(block[i], block[stack[-1]]) - block[top]

        answer += (distance * height)
    stack.append(i)

print(answer)