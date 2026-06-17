class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftindex = 0
        rightindex = 1

        for num1 in nums:
            for num2 in range(rightindex, len(nums)):
                if num1 + nums[num2] == target:
                    return [leftindex, num2]
            leftindex += 1
            rightindex += 1
            