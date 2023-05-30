
# 💡 **Q6.** Given an integer array nums, return true if any value appears at least twice
#  in the array, and return false if every element is distinct.

# **Example 1:**
# Input: nums = [1,2,3,1]

# Output: true
nums = [1, 2, 3, 1]

a = {}
for i in nums:
    if i in a.keys():
        print(True)
        break
    else:
        a[i] = 0
else:
    print(False)
