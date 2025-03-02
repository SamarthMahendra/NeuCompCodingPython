class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, start, end in trips:
            events.append((start, num))
            events.append((end, -num))

        events.sort(key=lambda x: (x[0], x[1]))

        current_passengers = 0
        for _, change in events:
            current_passengers += change
            if current_passengers > capacity:
                return False

        return True
