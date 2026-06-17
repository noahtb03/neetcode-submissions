class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sdict = {}
            tdict = {}
            for num in range(len(s)):
                sdict[s[num]] = sdict.get(s[num], 0) + 1
                tdict[t[num]] = tdict.get(t[num], 0) + 1

            return sdict == tdict

        else:
            return False