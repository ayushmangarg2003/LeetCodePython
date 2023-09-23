class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    v1 = version1.split('.')
    v2 = version2.split('.')
    n = max(len(v1), len(v2))
    for i in range(n):
        r1 = int(v1[i]) if i < len(v1) else 0
        r2 = int(v2[i]) if i < len(v2) else 0
        if r1 < r2:
            return -1
        elif r1 > r2:
            return 1
    return 0
