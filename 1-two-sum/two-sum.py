class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for outer_index in range(len(nums)):
            for inner_index in range(outer_index + 1, len(nums)):
                # print('[' + str(outer_index) + ', ' + str(inner_index) + ']')
                if nums[outer_index] + nums[inner_index] == target:
                    return [outer_index, inner_index]
