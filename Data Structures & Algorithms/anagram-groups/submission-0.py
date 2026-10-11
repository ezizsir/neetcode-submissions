class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = {}

        for word in strs:
            if self.letterHash(word) in memory:
                memory[self.letterHash(word)].append(word)
                continue
            memory[self.letterHash(word)] = [word]
            
        return list(memory.values())

    def letterHash(self, string):
        count = [0]*26
        word = list(string)
        for letter in word:
            count[ord(letter) - ord('a')] += 1

        return tuple(count)