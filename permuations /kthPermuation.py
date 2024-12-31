from typing import List
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n+1))
        k = k - 1
        permutation = ""

        for i in range(n):
            index = k // math.factorial(n - i - 1)
            permutation = permutation + str(numbers.pop(index))
            k %= math.factorial(n - i - 1)
        return permutation

