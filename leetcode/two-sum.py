# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value2index = {}
        for i, val in enumerate(nums):
            j = value2index.get(target - val)
            if j is not None: 
                return [j, i]
            value2index[val] = i

