class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_sort(log):
            if log[-1].isnumeric():
                return (1,)
            else:
                left , right = log.split(" ",1)
                return (0, right, left)
        return sorted(logs, key=custom_sort)
