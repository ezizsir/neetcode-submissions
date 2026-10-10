class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        familiar = set()

        for i in nums:
            if i in familiar:
                return True
            else:
                familiar.add(i)
        return False