def twoSum(nums, target):
    for i in range(int(target/2)):
        print(range(int(target/2)))
        if i in nums and target-i in nums:
            return [nums.index(i),nums.index(target-i)]
    return []

print(twoSum([3,2,4],6))

