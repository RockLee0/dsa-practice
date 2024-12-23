def containsDuplicate(nums):
    for i in range(len(nums)):
        initial_value=nums[i]
        for i in nums:
            if initial_value==i:
                return True
    return False
print(containsDuplicate([1,2,3]))
