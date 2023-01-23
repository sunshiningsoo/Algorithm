# https://school.programmers.co.kr/learn/courses/30/lessons/132267
def solution(a, b, n):
    answer = 0
    while n:
        answer += b
        n -= a
        n += b
        if n < a:
            break

    return answer