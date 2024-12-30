class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i

        return False

    def a(self):
        return 'fuck you'

    class Solution:

        def removeElement(self, nums: List[int], val: int) -> int:

            index = 0

            for i in range(len(nums)):

                if nums[i] != val:
                    nums[index] = nums[i]

                    index += 1

            return index
