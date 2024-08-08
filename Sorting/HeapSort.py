import heapq

def heapsort(arr):
    result = []
    heapq.heapify(arr)
    while arr:
        result.append(heapq.heappop(arr))
    return result


arr = [1,2, 6, 2, 3,5 ,0, 7, 5]

print(heapsort(arr))
