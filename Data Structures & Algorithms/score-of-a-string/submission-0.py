class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for loc, char in enumerate(s):
            if loc + 1 < len(s):
                score += abs(ord(char) - ord(s[loc + 1]))

        return score
