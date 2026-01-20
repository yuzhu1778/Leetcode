class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer={}
        for i, j in enumerate(nums):
            compliment= target -j
            if compliment in answer:
                return [answer[compliment],i]
            answer[j]=i
