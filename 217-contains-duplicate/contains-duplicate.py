class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found_elements = set() # look up time will be faster, so using set()

        for num in nums:
            if num not in found_elements:
                found_elements.add(num)
            else:
                return True # duplicate found

        return False