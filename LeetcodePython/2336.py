class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [i+1 for i in range(1000)]

    def popSmallest(self) -> int:
        # if len(self.arr) == 0:
        #     return 
        temp = min(self.arr)
        self.arr.remove(temp)
        return temp

    def addBack(self, num: int) -> None:
        if num not in self.arr:
            self.arr.append(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
