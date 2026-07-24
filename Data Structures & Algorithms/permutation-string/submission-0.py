class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        need = Counter(s1)
        
        for i in range(len(s2) - n + 1):
            if Counter(s2[i:i+n]) == need:
                return True

        return False