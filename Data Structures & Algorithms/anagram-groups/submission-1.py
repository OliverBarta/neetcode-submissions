class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        finalList = []
        def isAnagram(s1, s2):
            if s1 == "EMPTY" or s2 == "EMPTY":
                return False
            if len(s2) != len(s1):
                return False
            for letter in s2:
                if s2.count(letter) != s.count(letter):
                    return False
            return True
        
        
        for s in strs:
            if s == "EMPTY":
                continue
            subList = []
            for s2 in strs:
                if isAnagram(s, s2):
                    subList.append(s2)
                    strs[strs.index(s2)] = "EMPTY"
            finalList.append(subList)
        return finalList        