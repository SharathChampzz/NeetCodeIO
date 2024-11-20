class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_count = {}

        def is_anagram(s1, s2):
            nonlocal freq_count

            if len(s1) != len(s2):
                return False
            
            def get_freq(string):
                freq = defaultdict(int)

                for s in string:
                    freq[s] += 1
                
                freq_count[string] = freq # cache it for next run
                return freq_count[string]

            s1_freq = freq_count.get(s1) or get_freq(s1)
            s2_freq = freq_count.get(s2) or get_freq(s2)

            return s1_freq == s2_freq

        groupings = defaultdict(list)

        for s in strs:
            for key in groupings.keys():
                if is_anagram(s, key):
                    groupings[key].append(s)
                    break # anagram found
            else:
                groupings[s] = [s]

        return list(groupings.values())

