# TwoSum

def TwoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return[seen[complement], i]
        seen[nums[i]] = i
print(TwoSum([2,7,11,15],9))