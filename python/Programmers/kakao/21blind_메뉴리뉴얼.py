# 1. 존재하는 알파벳 구하고, course 갯수에 맞는 메뉴 조합을 구한다.
answer = []
tempAnswer = []

def solution(orders, course):
    global tempAnswer
    each_alphas = []
    total_alpha_set = set()
    for i in range(len(orders)):
        dic = {}
        for j in range(ord('A'), ord('Z') + 1):
            dic[chr(j)] = 0
        for k in orders[i]:
            dic[k] = 1
            total_alpha_set.add(k)
        each_alphas.append(dic)
    total_alpha_set = list(total_alpha_set)
    total_alpha_set.sort()

    def check(strs):
        global answer
        realTemp = 0
        for idx, each in enumerate(each_alphas):
            temp = 0
            for alpha in strs:
                temp += each[alpha]
            if temp == len(strs):
                realTemp += 1

        if realTemp >= 2:
            return [True, realTemp]
        return [False, 0]

    strSet = set()
    def combi2(cur, ptr, targetLen, order):
        global tempAnswer
        if len(cur) == targetLen and cur not in strSet:
            temp = check(cur)
            strSet.add(cur)
            if temp[0]:
                tempAnswer.append([cur, temp[1]])
            return
        for i in range(ptr, len(order)):
            combi2(cur+order[i], i+1, targetLen, order)


    for target in course:
        tempAnswer = []
        for order in orders:
            order = "".join(sorted(order))
            combi2("", 0, target, order)
        if tempAnswer:
            tempAnswer.sort(key=lambda x:(-x[1], x[0]))
            k = tempAnswer[0][1]
            for i in tempAnswer:
                if i[1] == k:
                    answer.append(i[0])
                else:
                    break

    answer.sort()

    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))