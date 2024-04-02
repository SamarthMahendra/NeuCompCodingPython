class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1

        d2 = {}
        for i in t:
            if i in d2:
                d2[i] =d2[i] +1
            else:
                d2[i] = 1
        for i, v in d.items():
            if i not in d2:
                return False
            if v != d2[i]:
                return False
        for i, v in d2.items():
            if i not in d:
                return False
            if v != d[i]:
                return False
        return True


    def isAnagram2(self, x: str, t: str) -> bool:
        s= list(t)
        j=0
        for i in range(len(x)):
                try:
                    s.remove(x[i])
                    j=j+1
                except:
                    continue
        if s or j<len(x):
            return False
        else:
            return True

    def isAnagram3(self, x: str, t: str) -> bool:
        return sorted(x) == sorted(t)


obj = Solution()
print(obj.isAnagram3("anagram", "nagaram"))