

# schedule - sequential , non overlapping dance sessions for (actors and actresses)
# decides sessions that camille can take and which she can assign it to her assistant
# camille - 2 shift ( separated by lunch break)
# each shift same no of sessions
# each session - different no of students
# camille's assistant will teach the sessions that are scheduled before camille's first shift, after camille's second shift, and during camille's lunch break
# lunch break can accomodate 1 session
# can not reoder the sessions



# maximize total no of students that camille can teach



# shift length is n ( number of sessions she can take in a shift)
# schedule = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# can not reorder the sessions

# algorithm used - dynamic programming


from typing import List

class Solution:
    def maxStudents(self, schedule: List[int]) -> int:
        n = len(schedule)
        m = n // 2
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(n):
                if schedule[j] & schedule[j - 1] == 0 and dp[i - 1][j - 1] != -1:
                    for k in range(n):
                        if schedule[j] & (1 << k) and dp[i - 1][j - 1 - k] != -1:
                            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1 - k] + bin(schedule[j]).count('1'))
        return max(dp[m])


n = 2
schedule = [1, 4, 3, 6, 9, 7, 2]
s = Solution()
print(s.maxStudents(schedule))  # Output: 12



#
# class RecursiveSolution:
#     def maxStudents(self, schedule: List[int]) -> int:
#         n = len(schedule)
#         m = n // 2
#         @lru_cache(None)
#         def dp(i, j):
#             if i == 0:
#                 return 0
#             if j == 0:
#                 return -1
#             if schedule[j - 1] & schedule[j - 2] == 0 and dp(i - 1, j - 2) != -1:
#                 return max(dp(i, j - 1), dp(i - 1, j - 2) + bin(schedule[j - 1]).count('1'))
#             return dp(i, j - 1)
#         return dp(m, n)
#
#



