# https://leetcode.com/problems/3sum/description/
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    answer.append(temp)
                    lastj = j
                    lastk = k
                    while j < k and nums[j] == nums[lastj]:
                        j += 1
                    while j < k and nums[k] == nums[lastk]:
                        k -= 1
                elif summ < 0:
                    j += 1
                else:
                    k -= 1

        return answer


# DFS를 활용한 발악..

# class Solution:
#
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         isVisited = [0] * len(nums)
#         count = 0
#         answer = []
#         temp = []
#
#         def answerInput(isVisited, nums):
#             temp = []
#             for i in range(len(isVisited)):
#                 if isVisited[i]:
#                     temp.append(nums[i])
#             if sum(temp) != 0:
#                 return
#             temp.sort()
#             if temp not in answer:
#                 answer.append(temp)
#
#         def DFS(start, count, isVisited, nums):
#             if count == 3:
#                 answerInput(isVisited, nums)
#                 return
#             for i in range(start, len(nums)):
#                 if isVisited[i] != 1:
#                     isVisited[i] = 1
#                     DFS(i, count + 1, isVisited, nums)
#                     isVisited[i] = 0
#
#         DFS(0, count, isVisited, nums)
#
#         return answer
