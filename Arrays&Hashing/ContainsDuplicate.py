'''
Given an integer array nums, return true  if any value appears at least twice in the array, and return false if every element is distinct
'''

class Solution(object):
    def containsDuplicate(self,nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        for i in nums:
            if i < len(nums):
        """

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    

p = Solution()

print(Solution.containsDuplicate(p, [1,2,3,4]))