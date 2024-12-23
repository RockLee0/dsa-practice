def containsDuplicate(nums):
    for i in range(len(nums)):
        initial_value=nums[i] #3
        print(i) #3
        for j_index, j in enumerate(nums):
            if initial_value==j and i != j_index:
                print(initial_value)
                print('dddd')
                return True
    print(f'i is :{initial_value}')
    return False
print(containsDuplicate([1,2,3,3]))


def contain(nums):
    distinct=set(nums)
    if len(nums)==len(distinct):
        return False
    else:
        return True

print(contain([1,2,2,3,4]))





