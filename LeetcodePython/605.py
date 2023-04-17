class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 1
        beds = 0
        for bed in flowerbed:
            if bed:
                count = 0
            else:
                count += 1
                if count == 3:
                    beds += 1
                    count = 1
        if not flowerbed[-1]: 
            count += 1
            if count == 3: beds += 1

        return beds >= n
