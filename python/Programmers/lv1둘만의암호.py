# https://school.programmers.co.kr/learn/courses/30/lessons/155652
def solution(s, skip, index):
    answer = ''
    alphabet = []
    maintemp = index

    for alphabet in s:
        maintemp = index
        temp = alphabet
        while maintemp:
            temp = chr(ord(temp) + 1)
            if temp is chr(ord('z') + 1):
                temp = 'a'
            if temp not in skip:
                maintemp -= 1


        answer += temp

    return answer


solution('asdgasdf', 'abcd', 5)