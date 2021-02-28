def merge(array, left, mid, right):
    left_part = array[left:mid + 1]

    right_part = array[mid + 1:right + 1]

    left_start = 0
    right_start = 0
    array_start = left

    while left_start < len(left_part) and right_start < len(right_part):
        if left_part[left_start] <= right_part[right_start]:
            array[array_start] = left_part[left_start]
            left_start += 1
        else:
            array[array_start] = right_part[right_start]
            right_start += 1
        array_start += 1

    while left_start < len(left_part):
        array[array_start] = left_part[left_start]
        left_start += 1
        array_start += 1

    while right_start < len(right_part):
        array[array_start] = right_part[right_start]
        right_start += 1
        array_start += 1


def merge_sort_aux(array, left, right):
    if left < right:
        mid = left + (right - left)//2
        merge_sort_aux(array, left, mid)
        merge_sort_aux(array, mid + 1, right)
        merge(array, left, mid, right)


def mergeSort(array):
    merge_sort_aux(array, 0, len(array) - 1)
    return array
