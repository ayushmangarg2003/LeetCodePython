class Solution:
    def bulky(self,length , width ,height):
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or length*width*height >= 10**9:
            return True
        return False
    def heavy(self,mass):
        if mass>=100:
            return True
        return False
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulk = self.bulky(length, width, height)
        heav = self.heavy(mass)
        if bulk and heav:
            return "Both"
        elif not bulk and not heav:
            return "Neither"
        elif bulk and not heav:
            return "Bulky"
        else:
            return "Heavy"
