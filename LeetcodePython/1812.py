class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        ref = {
            "a":1,
            "b":2,
            "c":3,
            "d":4,
            "e":5,
            "f":6,
            "g":7,
            "h":8
        }
        temp = ref[coordinates[0]]
        if (int(temp) + int(coordinates[1]))%2 == 0 :
            return 0
        return 1
