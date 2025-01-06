class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        curr = []
        for i in target:
            press = ord(i) - ord('a')
            curr.append('a')
            ans.append("".join(curr))
            for j in range(1, press+1):
                curr.pop()
                curr.append(chr(j + ord('a')))
                ans.append("".join(curr))
        return ans
