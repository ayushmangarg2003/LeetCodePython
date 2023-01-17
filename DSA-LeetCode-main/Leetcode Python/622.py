class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.q.append(value)
            return True 
        
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.q.pop(0)
            return True
            
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[0]
        
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[-1]
    
    def isEmpty(self) -> bool:
        return len(self.q) == 0
        
    def isFull(self) -> bool:
        return len(self.q) == self.k
