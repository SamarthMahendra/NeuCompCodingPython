class Solution:
    def romanToInt(self, s: str) -> int:
        ref_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev_value, total = 0, 0
        for r in reversed(s):
            if (value := ref_map[r]) < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total