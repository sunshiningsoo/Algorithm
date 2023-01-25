# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rangeNum = []
        for i in strs:
            rangeNum.append(len(i))
        answer = ''
        for i in range(min(rangeNum)):
            temp = strs[0][i]
            count = 0
            for k in strs:
                if k[i] == temp:
                    count += 1
                else:
                    return answer
            if count == len(strs):
                answer += strs[0][i]

        return answer

