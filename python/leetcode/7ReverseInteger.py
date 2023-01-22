# https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or -2**31 > x or (2)**31 < x-1:
            return 0
        while True:
            if x % 10 is not 0:
                break
            else:
                x //= 10

        tempString = str(x)
        temp = ''
        if tempString[0] == '-':
            for i in range(len(tempString)-1):
                temp += tempString[len(tempString) - i - 1]
            temp = '-' + temp
        else:
            for i in range(len(tempString)):
                temp += tempString[len(tempString) - i - 1]

        if -2**31 < int(temp) < 2**31 -1 :
            return int(temp)
        else:
            return 0