# https://www.acmicpc.net/problem/1747
N = int(input())

def isPrime(n):
    if n == 1:
        return 0
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return 0
    return 1

def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return 1
    return 0

# for i in range(N, 1000001):

while True:
    if isPalindrome(N):
        if isPrime(N):
            print(N)
            break
    N += 1
