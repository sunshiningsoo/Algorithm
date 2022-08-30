line = int(input())

arr = [0] * line # 1차원 배열로 생각함으로, 같은 열에 퀸을 놓는다는 가정자체를 배제
answer = 0

def check(count):
    for k in range(count):
        if arr[k] == arr[count] or abs(arr[count] - arr[k]) == count - k: # count - k 는 항상 양수 값
            return False
    return True

def dfs(count):
    global answer
    if count == line:
        answer += 1
        return
    else:
        for i in range(line):
            arr[count] = i
            if check(count): # 이전에 놓은 퀸들과 비교해서 내가 놓아도 되는지 판단하는 함수
                dfs(count + 1)

dfs(0)

print(answer)
