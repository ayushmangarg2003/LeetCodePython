class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        next_index = lambda j : (startIndex + j) % n
        prev_index = lambda j : (startIndex - j + n) % n

        steps = 0
        
        while steps < n:
            if words[next_index(steps)] == target or words[prev_index(steps)] == target:
                return steps
            steps += 1
        return -1
