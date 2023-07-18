# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = 0
    cloth = [1] * n
    for i in lost:
        cloth[i-1] = 0
    for i in reserve:
        cloth[i-1] += 1

    for i in range(n):
        if cloth[i] == 2 and i >= 1:
            if cloth[i-1] == 0:
                cloth[i] = 1
                cloth[i-1] = 1
        if cloth[i] == 2 and i < n-1:
            if cloth[i+1] == 0:
                cloth[i] = 1
                cloth[i + 1] = 1

    for i in cloth:
        if i >= 1:
            answer += 1

    return answer