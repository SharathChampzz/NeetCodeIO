class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict() # we need index too, so using dict

        for index, num in enumerate(nums):
            reminder = target - num

            if reminder in visited:
                return [visited[reminder], index]

            visited[num] = index # store this as visited, so that we can lookup later
        