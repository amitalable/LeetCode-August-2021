from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for st in strs:
            x = "".join(sorted(st))
            if x in hashMap.keys():
                hashMap[x].append(st)
            else:
                hashMap[x] = [st]
        return list(hashMap.values())


print(Solution().groupAnagrams(["a"]))
