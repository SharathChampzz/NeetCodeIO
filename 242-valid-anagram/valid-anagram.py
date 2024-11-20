class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # if length are not same, it means. We cannot make valid anagram

        mapping_s = defaultdict(int) # using default dict, so that we dont have to handle doesnot exist case
        mapping_t = defaultdict(int)

        # build mapping
        for index in range(len(s)):
            mapping_s[s[index]] += 1
            mapping_t[t[index]] += 1

        # validate if both the dict are same or not
        return mapping_s == mapping_t


        