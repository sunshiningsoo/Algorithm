N = int(input())

arr = [0] * (N+1)

# 3으로 나눠 떨어지면 나누기
# 2로 나눠 떨어지면 나누기
# 1을 뺀다
# while N != 1:
#     if N % 3 == 0:
#         arr[int(N/3) - 1] += 1
#         N = int(N/3)
#     elif N % 2 == 0:
#         arr[int(N/2)- 1] += 1
#         N = int(N/2)
#     else:
#         arr[int(N-1)] = 1
#         N -= 1
#
# print(sum(arr))

# 아래에서부터 올라가며, N이 될때 그 수가 어떤 값을 가지고 있는지 본다. min값을 계속해서 업데이트해주는 과정이 dynamic programming 과정으로 들어가 있다.
for i in range(2, N+1):
    arr[i] = arr[i-1] + 1 # 가장 변화폭이 큰 +1의 경우를 가장 상위에 둔다.
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)

print(arr[N])