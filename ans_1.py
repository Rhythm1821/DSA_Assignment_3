def threeSumClosest(nums, target):
    nums.sort()
    closestSum = float('inf')

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                return target

    return closestSum
print(threeSumClosest( [-1,2,1,-4], 1))