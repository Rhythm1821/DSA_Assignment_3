def nextPermutation(nums):
    # Find the first decreasing element from the right
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Find the smallest element larger than nums[i] from the right
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the suffix from i+1 onwards
    left = i + 1
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
print(nextPermutation([1,2,3]))