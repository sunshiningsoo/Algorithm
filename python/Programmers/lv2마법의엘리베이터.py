# https://school.programmers.co.kr/learn/courses/30/lessons/148653
# 5일때의 edge케이스를 생각해주자!
def solution(storey):
    answer = 0
    while storey > 0:
        temp = str(storey)
        if int(temp[-1]) == 5 and len(temp) >= 2:
            if int(temp[-2]) >= 5:
                n = 10 - int(temp[-1])
                answer += n
                storey += n
            else:
                n = int(temp[-1])
                answer += n
                storey -= n
        else:
            if int(temp[-1]) > 5:
                n = 10 - int(temp[-1])
                answer += n
                storey += n
            else:
                answer += int(temp[-1])
                storey -= int(temp[-1])
        storey //= 10

    return answer