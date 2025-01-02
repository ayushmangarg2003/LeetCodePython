class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = 'aeiou'
        prefix = [0] * (len(words)+1)
        
        for i in range(len(words)):
            prefix[i+1] = prefix[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i+1] += 1

        ans = []
        for i in queries:
            ans.append(prefix[i[1]+1] - prefix[i[0]])
        return ans
