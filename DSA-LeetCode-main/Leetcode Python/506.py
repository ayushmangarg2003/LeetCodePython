class Solution:
		def findRelativeRanks(self, score: List[int]) -> List[str]:
			ans=[]
			duplicate=sorted(score , reverse=True) 
			for i in range(len(score)): 
				if score[i]==duplicate[0]:
					ans.append("Gold Medal")
				elif score[i]==duplicate[1]:
					ans.append("Silver Medal")
				elif score[i]==duplicate[2]:
					ans.append("Bronze Medal")
				else:
					ans.append(str((duplicate.index(score[i]))+1)) 
			return ans 
