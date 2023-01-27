# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        ans = []
        tempAns = ''
        if digits is "":
            return ans
        word = ''

        def DFS(i, word):
            if i == len(digits):
                ans.append(word)
                return

            for j in dic[int(digits[i])]:
                word += j
                DFS(len(word), word)
                word = word[:-1]

        DFS(0, '')
        return ans

