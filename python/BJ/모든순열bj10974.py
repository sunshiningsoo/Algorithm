N = int(input())

temp = []

def track():
    if len(temp) == N:
        for num in temp:
            print(num, end=" ")
        print()
    for i in range(1, N+1):
        if i not in temp:
            temp.append(i)
            track()
            temp.pop()

track()