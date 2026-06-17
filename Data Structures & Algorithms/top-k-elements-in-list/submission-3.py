class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqDict = counts.most_common(k)
        freqArr = []

        for num, value in freqDict:
            freqArr.append(num)

        return freqArr