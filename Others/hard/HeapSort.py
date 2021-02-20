import heapq


def heapSort(array):
    array = [-x for x in array]
    heapq.heapify(array)

    result = []

    while len(array):
        result.insert(0, -heapq.heappop(array))

    return result
