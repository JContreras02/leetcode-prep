# -------Brute Force Attempt-------- O(n^2)
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# O(n) time complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, num in enumerate(nums):
            diff =  target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i






















"""
        tracker = {}

        # i index, n value of list
        for i, n in enumerate(nums):
            diff = target - n
            if diff in tracker:
                return [tracker[diff], i]
            tracker[n] = i




"""
