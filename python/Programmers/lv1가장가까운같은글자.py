# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    dic = {}
    count = 0
    answer = []
    tempAnswer = []
    for i in s:
        if i not in tempAnswer:
            tempAnswer.append(i)
            dic[i] = count
            answer.append(-1)
        else:
            answer.append(count - dic[i])
            dic[i] = count

        count += 1

    return answer