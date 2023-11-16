N = int(input())
alphaDic = {}

dic = [0]*26

for i in range(N):
    parent, left, right = map(str, input().split())
    alphaDic[parent] = [left, right]

def front(current):
    print(current, end="")
    for alpha in alphaDic[current]:
        if alpha == '.':
            continue
        front(alpha)


def middle(current):
    if current == '.':
        return
    middle(alphaDic[current][0])
    print(current, end="")
    middle(alphaDic[current][1])


def last(current):
    for alpha in alphaDic[current]:
        if alpha == '.':
            continue
        last(alpha)
    print(current, end="")


front("A")
print()
middle("A")
print()
last("A")

