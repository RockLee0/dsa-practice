#wrong approach
def twoSum(nums, target):
    if target==0:
        for j in nums:
            if j==0:
                return [nums.index(j), nums.index(j, nums.index(j) + 1)]
            if -j in nums:
                return [nums.index(j),nums.index(-j)]
    else:
        for i in nums:
            if target - i in nums:
                if i!=target-i:
                    return [nums.index(i), nums.index(target - i)]
                else: return [nums.index(i),nums.index(i,nums.index(i)+1)]
        return []


print(twoSum([0,4,3,0],0))
print(twoSum([-1,-2,-3,-4,-5],-8))
print(twoSum([3,3],6))


#right approach
def twoSum_(n,t):
    s={}
    for index,i in enumerate(n):
        if t-i in s:
            return [s[t-i],index]
        s[i]=index
    return []
print(twoSum_([0,4,3,0],0))


