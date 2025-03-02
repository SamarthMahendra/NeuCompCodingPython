class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        visited = [False] * n

        res = []

        def backtrack(cur=[]):
            if len(cur) == n:
                res.append(cur.copy())

            for i in range(n):
                if visited[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1]:
                    continue

                visited[i] = True
                newcur = cur + [nums[i]]
                backtrack(newcur)
                visited[i] = False
            return

        backtrack()
        return res


