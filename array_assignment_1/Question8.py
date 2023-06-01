
# 💡 **Q8.** You have a set of integers s, which originally contains all the numbers from
#  1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another
# number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.


# Find the number that occurs twice and the number that is missing and return them in the form
#  of an array.

# **Example 1:**
# Input: nums = [1,2,2,4]
# Output: [2,3]
///

nums = [1, 2, 2, 4]
n = len(nums)
for i in range(1, n+1):
    if i not in nums:
        break
add = (sum(nums)+i)-(n*(n+1)//2)
        
print([add, i])
