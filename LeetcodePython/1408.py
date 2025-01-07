# This one worked but has is own edge case for ex ['leet','code','leetc']
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = ' '.join(words)
        subStr = [i for i in words if arr.count(i) >= 2]
        return subStr

#  Better Solution
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i!=j:
                    ans.append(words[i])
        return list(set(ans))
