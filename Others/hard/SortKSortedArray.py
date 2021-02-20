import heapq


def sortKSortedArray(array, k):
    # Write your code here.
    heap = []
    result = []

    for elem in array:
        heapq.heappush(heap, elem)
        if len(heap) == k + 1:
            result.append(heapq.heappop(heap))
    while len(heap):
        result.append(heapq.heappop(heap))
    return result
