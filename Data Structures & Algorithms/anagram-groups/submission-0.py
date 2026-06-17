class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        stringdict = defaultdict(list)
        finalList = []

        for string in strs:
            sortedStr = "".join(sorted(string))
            stringdict[sortedStr].append(string)
        
        for key, value in stringdict.items():
            finalList.append(value)

        return finalList