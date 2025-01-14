
class Solution(object):
    def scoreOfString(self, s):
        local_ord = ord
        sum = 0
        n = len(s)
        for i in range( n -1):
            sum += abs(
                local_ord(s[i]) - local_ord(s[ i +1])
            )
        return sum


print(Solution().scoreOfString("helloworld"))