class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dict:
                return [dict[temp], i]
            dict[nums[i]] = i
