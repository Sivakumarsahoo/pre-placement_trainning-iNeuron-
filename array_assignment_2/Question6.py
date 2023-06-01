# Question 6
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index.Otherwise,
# return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4

# Explanation: 9 exists in nums and its index is 4

nums = [-1, 0, 3, 5, 9, 12]
target = 8
start = 0
end = len(nums)-1
while (start <= end):
    mid = (start+end)//2
    if (nums[mid] == target):
        print(mid)
        break
    elif (nums[mid] > target):
        end = mid-1
    else:
        start = mid+1
else:
    print(-1)
