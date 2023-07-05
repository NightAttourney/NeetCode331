# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#The point of this problem is to make sure that you know how to properly use enumerate or know how to code it in another language
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}

        for i, n in enumerate(nums): #enumerating this way cause you need the index and value in a single pass
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i


solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))

