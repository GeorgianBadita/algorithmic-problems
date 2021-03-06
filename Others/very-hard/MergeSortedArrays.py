import heapq


def mergeSortedArrays(arrays):
    heap = []

    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    result = []
    while heap:
        element, array_index, position_in_array = heapq.heappop(heap)
        result.append(element)
        if position_in_array + 1 < len(arrays[array_index]):
            heapq.heappush(
                heap,
                (arrays[array_index][position_in_array + 1], array_index, position_in_array + 1))

    return result
