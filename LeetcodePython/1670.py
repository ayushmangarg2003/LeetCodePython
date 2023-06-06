class FrontMiddleBackQueue:

    def __init__(self):
        self.q = []

    def pushFront(self, val: int) -> None:
        self.q.insert(0,val)        

    def pushMiddle(self, val: int) -> None:
        n=len(self.q)
        if n%2==0:
            n=(n/2)
        else:
            n=int(n//2)
        i=0
        self.q.insert(int(n),val)
        print(self.q)

    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        if len(self.q)==0:
            return -1
        l=self.q[0]
        del self.q[0]
        return l

    def popMiddle(self) -> int:
        if len(self.q)==0:
            return -1
        n=len(self.q)
        if n%2==0:
            n=(n/2)-1
        else:
            n=n//2
        p=self.q[int(n)]
        del self.q[int(n)]
        return p

    def popBack(self) -> int:
        if len(self.q)==0:
            return -1
        p=self.q[len(self.q)-1]
        del self.q[len(self.q)-1]
        return p
