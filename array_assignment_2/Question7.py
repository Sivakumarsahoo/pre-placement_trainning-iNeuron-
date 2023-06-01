# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
# monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example 1:
# Input: nums = [1, 2, 2, 3]
# Output: true

def isMonotonic( nums):
    if len(nums) == 1:
        return True
    if nums[0] >= nums[len(nums)-1]:
        for i in range(0, len(nums)-1):
            if nums[i] < nums[i+1]:
                return False
    else:
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
    return True


nums = [1, 2, 2, 3]
print(isMonotonic(nums))