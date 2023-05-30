# 💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index
#  if the target is found. If not, return the index where it would be if it were inserted in
#  order.

# You must write an algorithm with O(log n) runtime complexity.

# **Example 1:**
# Input: nums = [1,3,5,6], target = 5

# Output: 2
nums=[1,3,5,6]
first = 0
target=2
end = len(nums)-1
while (first <= end):
    mid = (first+end)//2
    if nums[mid] > target:
        end = mid-1
    elif nums[mid] < target:
        first = mid+1
    else:
        print(mid)
        break
else:
    print(first)
