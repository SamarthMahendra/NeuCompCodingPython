class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        return bin(res).count('1')