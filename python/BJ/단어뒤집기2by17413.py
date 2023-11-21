a = input()

idx = 0
q = []
backq = []
answer = []
if len(a) == 0:
    print("")
    exit()

printq = []
while idx != len(a):
    if a[idx] == "<":
        if len(printq)!= 0:
            q += printq[::-1]
            printq = []
        while a[idx] != ">":
            q.append(a[idx])
            idx += 1
        q.append(">")
    else:
        if a[idx] == " ":
            q += printq[::-1]
            q.append(" ")
            printq = []
        else:
            printq.append(a[idx])
    idx += 1

if len(printq) != 0:
    q += printq[::-1]
for i in q:
    print(i, end="")

