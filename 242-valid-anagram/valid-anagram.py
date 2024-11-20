class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping_s = defaultdict(int)
        mapping_t = defaultdict(int)

        # mapping for s
        for char in s:
            mapping_s[char] += 1

        # mapping for t
        for char in t:
            mapping_t[char] += 1

        # validate if both the dict are same or not
        return mapping_s == mapping_t


        