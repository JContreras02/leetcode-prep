# -------Brute Force Attempt-------- O(n^2)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sum([2, 3, 11, 7], 9))


