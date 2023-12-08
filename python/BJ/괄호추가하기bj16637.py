import sys
input = sys.stdin.readline
N = int(input())
sentence = list(input())

answer = -1e9

def simpleCalc(value, sentenceA):
    dap = 0
    if sentenceA[value] == '+':
        dap += int(sentenceA[value-1]) + int(sentenceA[value+1])
    elif sentenceA[value] == '-':
        dap += int(sentenceA[value - 1]) - int(sentenceA[value + 1])
    elif sentenceA[value] == '*':
        dap += int(sentenceA[value - 1]) * int(sentenceA[value + 1])
    return dap

def calc(points):
    tempSentence = sentence.copy()
    tempSentence = tempSentence[:-1]

    while points:
        a = points.pop()
        b = points.pop()
        tt = simpleCalc(b+1, sentence)
        tempSentence.pop(b)
        tempSentence.pop(b)
        tempSentence.pop(b)
        tempSentence.insert(b, tt)

    while len(tempSentence) >= 3:
        a = tempSentence.pop(0)
        b = tempSentence.pop(0)
        c = tempSentence.pop(0)
        realTemp = 0
        if b == '+':
            realTemp = int(a) + int(c)
        elif b == '-':
            realTemp = int(a) - int(c)
        elif b == '*':
            realTemp = int(a) * int(c)
        tempSentence.insert(0, realTemp)

    return int(tempSentence[0])


def check(arrPointers, cur):
    global answer
    if cur >= len(sentence) - 1:
        answer = max(answer, calc(arrPointers))
        return

    # 1. 지금 숫자와 바로 뒤 숫자를 묶어주거나
    if cur + 2 < len(sentence):
        check(arrPointers + [cur, cur + 2], cur + 4)

    # 2. 묶어주지 않을지
    check(arrPointers, cur + 2)


check([], 0)
print(answer)