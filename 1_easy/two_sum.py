# -------Brute Force Attempt-------- O(n^2)
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tracker = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in tracker:
                return [tracker[diff], i]
            tracker[n] = i

