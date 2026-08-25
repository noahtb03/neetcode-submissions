class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n

        while True:
            newNum = sum(int(i) ** 2 for i in str(num))
            if newNum in seen:
                return False
            elif newNum == 1:
                return True
            seen.add(newNum)
            num = newNum

        return False
