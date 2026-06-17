class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftindex = 0
        rightindex = 1

        for num in numbers:
            for i in range(rightindex, len(numbers)):
                if num + numbers[i] == target:
                    return [leftindex + 1, i + 1]

            rightindex += 1
            leftindex += 1