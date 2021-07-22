import math


def solution(progresses, speeds):
    re = []
    for i in range(len(progresses)):
        a = math.ceil((100 - progresses[i]) / speeds[i])
        re.append(a)
    answer = []
    num = 1
    for i in range(1, len(re)):
        if re[i - 1] >= re[i]:
            num += 1
        else:
            answer.append(num)
            num = 1
    answer.append(num)

    return answer

solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])