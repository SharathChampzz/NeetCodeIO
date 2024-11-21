class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1 # calculate frequency of each

        # sort based on the value in descending order
        desc_sort = sorted(freq.items(), key= lambda item: item[1], reverse=True)

        # pick the most k elements
        result = [desc_sort[i][0] for i in range(k)]

        return result
