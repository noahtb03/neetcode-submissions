class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for string in strs:
            encoded_str += str(len(string)) + "#" + string

        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i
            lengthstr = ""

            # read number
            while s[j] != "#":
                lengthstr += s[j]
                j += 1

            length = int(lengthstr)
            i = j + 1  # skip '#'

            # read actual string
            newstr = s[i:i + length]
            strs.append(newstr)

            i = i + length

        return strs
            


