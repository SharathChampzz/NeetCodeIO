class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        desc_sort = sorted(freq.items(), key= lambda item: item[1], reverse=True)

        result = [desc_sort[i][0] for i in range(k)]

        return result
