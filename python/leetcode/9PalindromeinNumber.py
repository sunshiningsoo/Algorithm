# https://leetcode.com/problems/palindrome-number/description/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == 0:
            return True

        tempString = str(x)
        for i in range(len(tempString) // 2):
            if tempString[i] != tempString[len(tempString) - 1 - i]:
                return False

        return True
