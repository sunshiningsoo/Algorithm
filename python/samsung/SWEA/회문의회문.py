N = int(input())

for i in range(1, N+1):
    munja = input()
    if munja != munja[::-1]:
        print(f"#{i} NO")
        continue
    munjaLen = len(munja)
    if munja[:munjaLen//2] != munja[:munjaLen//2][::-1]:
        print(f"#{i} NO")
        continue
    if munja[munjaLen//2+1:] != munja[munjaLen//2+1:][::-1]:
        print(f"#{i} NO")
        continue
    print(f"#{i} YES")


