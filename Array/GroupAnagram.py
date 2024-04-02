from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for i in range(len(strs)):
            d1 = self.charFrequency(strs[i])
            d1 = "".join(d1)
            if d1 in res:
                res[d1].append(strs[i])
            else:
                res[d1] = [strs[i]]
        r = []
        for k,v in res.items():
            r.append(v)
        return r

    def groupAnagramsv2(self, strs):
        res = {}
        for i in range(len(strs)):
            d1 = str(sorted(strs[i]))
            if d1 in res:
                res[d1].append(strs[i])
            else:
                res[d1] = [strs[i]]
        r = []
        for k,v in res.items():
            r.append(v)
        return r


    @staticmethod
    def charFrequency(st):
        # list containing 26 0's
        d = [''] * 26
        x  = []
        for i in st:
            if i in x:
                d[ord(i)-ord('a')] = str(int(d[ord(i)-ord('a')]) + 1)
            else:
                x.append(i)
                d[ord(i)-ord('a')] = '1'
        for j in range(len(d)):
            d[j] = chr(100+j) + d[j]
        return d

    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for i in strs:
            sorted_str = sorted(i)
            s = "".join(sorted_str)
            res[s].append(i)
        return list(res.values())


obj = Solution()
print(obj.groupAnagramsv2(["abbbbbbbbbbb","aaaaaaaaaaab"]))