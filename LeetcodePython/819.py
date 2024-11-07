class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation = ".,!?;:'\"()-"
        cleaned_text = ""
        for char in paragraph:
            if char in punctuation:
                cleaned_text += " "  
            else:
                cleaned_text += char

        cleaned_text = " ".join(cleaned_text.split())
        words = cleaned_text.lower().split(' ')
        c = Counter(words)
        c2 = [k for k,v in sorted(c.items(), key=lambda item: item[1], reverse=True)]
        for i in c2:
            if i not in banned:
                return i
