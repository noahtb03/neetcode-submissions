class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int(''.join(map(str, digits))) + 1
        return [int(d) for d in str(n)]