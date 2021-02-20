def partition(array, left, right):
    pivot = array[right]

    i = left - 1

    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def quick_sort_aux(array, left, right):
    if left < right:
        pi = partition(array, left, right)
        quick_sort_aux(array, left, pi - 1)
        quick_sort_aux(array, pi + 1, right)


def quickSort(array):
    quick_sort_aux(array, 0, len(array) - 1)
    return array
