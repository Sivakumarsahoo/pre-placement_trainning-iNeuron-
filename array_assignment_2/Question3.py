# Question 3
# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence
# among all its possible subsequences.

# A subsequence of an array is a sequence that can be derived from the array by deleting
# some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [1, 3, 2, 2, 5, 2, 3, 7]
# Output: 5

# Explanation: The longest harmonious subsequence is [3, 2, 2, 2, 3].


nums = [1, 3, 2, 2, 5, 2, 3, 7]
dict1 = {}
for i in nums:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        a = dict1[i]+1
        dict1[i] = a

b = list(dict1.keys())
b.sort()
ans = 0
for i in range(0, len(b)-1):
    if b[i]-b[i+1] == -1:
        ans = max(ans, dict1[b[i]]+dict1[b[i+1]])

print(ans)
