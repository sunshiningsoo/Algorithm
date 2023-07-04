# https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ''

        def check(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            # 홀수
            odd = check(s, i, i)

            # 짝수
            even = check(s, i, i + 1)

            if len(odd) > len(answer):
                answer = odd
            if len(even) > len(answer):
                answer = even

        return answer