class Allocator:

    def __init__(self, n: int):
        self.memory = [0]*n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0 
        for i in range(len(self.memory)): 
            if self.memory[i] == 0: 
                cnt += 1
                if cnt == size: 
                    break 
            else: 
                cnt = 0 
        else: 
            return -1 
        self.memory[i-size+1 : i+1] = [mID]*size
        return i-size+1        

    def free(self, mID: int) -> int:
        freed = 0
        for i in range(len(self.memory)):
            if self.memory[i]==mID:
                self.memory[i]= 0
                freed +=1
        return freed
        
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
