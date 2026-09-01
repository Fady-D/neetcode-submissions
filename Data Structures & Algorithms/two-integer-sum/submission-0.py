class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in my_map:
                return [my_map[difference], i]
            my_map[n] = i
