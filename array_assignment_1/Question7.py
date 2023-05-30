
# 💡 **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the
#  relative order of the nonzero elements.

# Note that you must do this in-place without making a copy of the array.

# **Example 1:**
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]



nums=[0,1,0,3,12]
i = 0
  # representing for zeroes
j = 0
    # representing for ones
    # [0,1,0,3,12]
    # [1,0,0,3,12]
    # [1,3,0,0,12]
while i <= j and j < len(nums):
    if nums[i] == 0 and nums[j] != 0:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
    elif(nums[i] != 0 and nums[j] == 0 or nums[i] != 0 and nums[j]!=0):
        i += 1
    j += 1
print(nums)
