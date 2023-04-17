class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dummy = []
        for i in words:
            temp = ""
            for j in i:
                temp+= morse[ord(j) - ord('a')]
            dummy.append(temp)
        return len(set(dummy))
                
