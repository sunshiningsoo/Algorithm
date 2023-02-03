# https://school.programmers.co.kr/learn/courses/30/lessons/155652
# 넘어가면 if문을 사용해 앞으로 옴겨주는 방식이 있지만,
# 조금 더 응용해보면, 배열의 길이만큼을 나눈 나머지라고 생각해도 된다.

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