# Question 5
# Given an integer array nums, find three numbers whose product is maximum and return
# the maximum product.

# Example 1:
# Input: nums = [1, 2, 3]
# Output: 6

import heapq
nums = [1, 2, 3]
heapq.heapify(nums)
a = heapq.nlargest(3, nums)
b = heapq.nsmallest(2, nums)
print( max(a[0]*a[1]*a[2], b[0]*b[1]*a[0]))