class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        let1 = sorted(s)
        let2 = sorted(t)
        if let1 == let2:
            return True
        return False