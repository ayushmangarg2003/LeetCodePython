class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = [] 
        self.maxx = maxSize

    def push(self, x: int) -> None:
        if len(self.arr) < self.maxx:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) == 0:
            return -1
        else:
            temp = self.arr[-1]
            self.arr = self.arr[0:len(self.arr)-1]
            return temp

    def increment(self, k: int, val: int) -> None:
        for i in range(0, min(len(self.arr), k)):
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
