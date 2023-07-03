# https://www.acmicpc.net/problem/5525

N = int(input())
S = int(input())
target = input()
answer = 0
P = 'IO'*N + 'I'
recent = False

# 50점짜리 풀이
# for i in range(len(target) - len(P) + 1):
#     if recent:
#         recent = False
#         continue
#     if target[i] == 'I':
#         if target[i:i+len(P)] == P:
#             answer += 1
#             recent = True
#             continue

# 100점짜이 풀이
# two pointer사용, 가망이 없는 값이면, left pointer를 옮겨버리고 끝내버림
left, right = 0, 0
while right < S:
    if target[right:right+3] == 'IOI':
        right += 2

        if right - left == 2*N:
            answer += 1
            left += 2
    else:
        right += 1
        left = right


print(answer)

