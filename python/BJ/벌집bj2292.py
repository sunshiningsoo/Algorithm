N = int(input())
k = 1
count = 1

while N > k:
    k += 6 * count
    count += 1

print(count)