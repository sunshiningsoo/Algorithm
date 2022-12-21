N = int(input())

first = 666
while N:
    if '666' in str(first):
        N -= 1
        first += 1
        continue
    first += 1

print(first - 1)
