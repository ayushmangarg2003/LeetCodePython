class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict1 = defaultdict(list) 
        for i in range(len(groupSizes)):
            dict1[groupSizes[i]].append(i)
        ans = []
        for k,v in dict1.items():
            temp = []
            for i in range(len(v)):
                if len(temp) == k:
                    ans.append(temp)
                    temp = []
                temp.append(v[i])
            ans.append(temp)
        return ans
