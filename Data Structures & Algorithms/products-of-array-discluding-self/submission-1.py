class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newnums = []

        for i, num in enumerate(nums):
            temp = nums[i]
            nums[i] = 1
            newnum = math.prod(nums)
            newnums.append(newnum)
            nums[i] = temp

        return newnums

