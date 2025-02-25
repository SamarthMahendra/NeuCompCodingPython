class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        tasks = Counter(tasks)
        tasks = [-v for i, v in tasks.items()]
        heapq.heapify(tasks)
        cooldown = []

        time = 0
        while tasks or cooldown:

            time += 1
            if tasks:
                temp = heapq.heappop(tasks) + 1
                if temp < 0:
                    cooldown.append((temp, time + n))
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(tasks, cooldown.pop(0)[0])
        return time


