class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            temp = str(n)
            n = 0
            for i in temp:
                n += int(i) * int(i)
            if n in seen:
                return False
            seen.add(n)

        return True





n = 19
obj = Solution()
print(obj.isHappy(n))