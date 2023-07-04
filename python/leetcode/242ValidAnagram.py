# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for i in s:
            if dic.get(i) is None:
                dic[i] = 1
            else:
                dic[i] += 1

        for j in t:
            if dic.get(j) is not None:
                if dic[j] == 0:
                    continue
                if t.count(j) == dic[j]:
                    dic[j] = 0
            else:
                return False

        if sum(list(dic.values())) != 0:
            return False

        return True
