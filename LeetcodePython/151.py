class Solution(object):
    def reverseWords(self, s):
        return " ".join(" ".join(s.split()).split(" ")[::-1])
