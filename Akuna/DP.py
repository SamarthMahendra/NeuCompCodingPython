

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


def optimize_schedule_dp(schedule, n):
    total_sessions = len(schedule)

    # If there aren't enough sessions for two shifts and a break, return 0
    if total_sessions < 2 * n + 1:
        return 0, [], schedule

    # Create a prefix sum array for efficient range sum queries
    prefix_sum = [0] * (total_sessions + 1)
    for i in range(1, total_sessions + 1):
        prefix_sum[i] = prefix_sum[i - 1] + schedule[i - 1]

    # Function to get sum of a range [start, end) using prefix sum
    def range_sum(start, end):
        return prefix_sum[end] - prefix_sum[start]

    # dp[i] represents the maximum students Camille can teach
    # if her first shift starts at index i
    dp = [0] * (total_sessions - 2 * n)

    for i in range(len(dp)):
        first_shift = range_sum(i, i + n)
        second_shift = range_sum(i + n + 1, i + 2 * n + 1)
        dp[i] = first_shift + second_shift

    # Find the starting index that gives maximum students
    best_start = max(range(len(dp)), key=lambda i: dp[i])
    max_students = dp[best_start]

    # Construct Camille's and assistant's schedules
    camille_sessions = schedule[best_start:best_start + n] + schedule[best_start + n + 1:best_start + 2 * n + 1]
    assistant_sessions = schedule[:best_start] + [schedule[best_start + n]] + schedule[best_start + 2 * n + 1:]

    return max_students, camille_sessions, assistant_sessions

n = 2
schedule = [1, 4, 3, 6, 9, 7, 2]
print(optimize_schedule_dp(schedule, n))  # 23



# #
#
# # return max students that can be taught by camille
# class RecursiveSolution:
#     def maxStudents(self, schedule: List[int]) -> int:
#         n = len(schedule)
#         m = n // 2
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
# n = 2
# schedule = [1, 4, 3, 6, 9, 7, 2]
# s = RecursiveSolution()
# print(s.maxStudents(schedule))  # Output: 12
