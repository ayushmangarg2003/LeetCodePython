class Solution(object):
    def sumZero(self, n):
        result = []
        count = 1
        count2 = -1
        if n%2==0:
            while len(result)!=n:
                result.append(count)
                count+=1
                result.append(count2)
                count2-=1
            return result
        else:
            result.append(0)
            while len(result)!=n:
                result.append(count)
                count+=1
                result.append(count2)
                count2-=1
            return result
            
            
