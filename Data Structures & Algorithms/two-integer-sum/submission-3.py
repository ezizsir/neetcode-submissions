class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        memory = {}

        for index, num in enumerate(nums):
            pair = target - num
            if pair in memory:
                return [memory[pair], index]
            memory[num] = index
        # make a hash table of the List
        # subtract the target from i in the nums
        # check for the other pair in hash table