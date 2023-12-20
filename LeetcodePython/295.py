class MedianFinder:
    def __init__(self):
        self.MedianFinder = []

    def addNum(self, num: int) -> None:
        self.MedianFinder.append(num)


    def findMedian(self) -> float:
        self.MedianFinder.sort()
        if len(self.MedianFinder)%2 ==0 :
            return (self.MedianFinder[len(self.MedianFinder)//2] + self.MedianFinder[(len(self.MedianFinder)//2)-1])/2
        return  self.MedianFinder[len(self.MedianFinder)//2] 
