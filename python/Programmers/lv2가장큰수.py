# https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])*4

    numbers.sort(reverse=True)
    print(numbers)
    for i in range(len(numbers)):
        temp = numbers[i]
        answer += temp[:len(temp)//4]

    if int(answer) == 0:
        return '0'

    return answer

solution([6, 10, 2])