# 주의해야 할 점. hap을 계속 해서 가져가서 hap보다 클 경우 업데이트 하는 형식으로 간다면
# hap이 앞 list의 값에 머물러 있을 수 있으므로 조심해야 한다.
N, K = map(int, input().split())

num = list(map(int, input().split()))

start = 0
end = K
hap = sum(num[start:end])
arr = [hap]

while True:
    if end == len(num):
        break
    arr.append(hap - num[start] + num[end])
    hap = hap - num[start] + num[end]
    start += 1
    end += 1

print(max(arr))
