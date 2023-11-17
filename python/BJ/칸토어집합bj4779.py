def kantoa(start, last):
    if last-start == 1:
        print('-', end='')
        return
    
    kantoa(start, int(last / 3))
    print(' '*int((last-start)/3), end='')
    # kantoa(int(last/ (2/3)), last)
    kantoa(start, int(last / 3))
    # 3부분으로 나눠야 함

while True:
    try:
        k = input()
        k = int(k)
        a = 3**k
        kantoa(0, a)
        print()
    except:
        break
    
