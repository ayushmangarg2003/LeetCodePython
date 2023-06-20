class Solution:
    def removeDigit(self, number: str, digit: str) -> str:        
        last_index = 0
        for num in range(1, len(number)):
            if number[num-1] == digit:
                if int(number[num]) > int(number[num-1]):
                    return number[:num-1] + number[num:]
                else:
                    last_index = num - 1
        if number[-1] == digit:
            last_index = len(number) - 1
        return number[:last_index] + number[last_index + 1:]
