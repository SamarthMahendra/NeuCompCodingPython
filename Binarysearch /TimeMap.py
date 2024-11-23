import bisect


class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int):
        # If the key doesn't exist in the map, initialize with an empty list
        if key not in self.map:
            self.map[key] = []
        # Append the value along with its timestamp to the list for the key
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return an empty string
        if key not in self.map:
            return ""

        # Get the list of (timestamp, value) tuples for the key
        values = self.map[key]

        # Perform binary search to find the largest timestamp <= the given timestamp
        idx = bisect.bisect_right(values, (timestamp, chr(127))) - 1

        # If idx is negative, it means no valid timestamp <= the requested timestamp
        if idx == -1:
            return ""

        # Return the value associated with the found timestamp
        return values[idx][1]
