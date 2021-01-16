def sameBsts(arr1, arr2):
    return same_bsts(arr1, arr2, 0, 0, float('-inf'), float('inf'))


def same_bsts(array1, array2, idx1, idx2, min_val, max_val):
    if idx1 == -1 or idx2 == -1:
        return idx1 == idx2

    if array1[idx1] != array2[idx2]:
        return False

    left_root_idx1 = get_first_smaller(array1, idx1, min_val)
    left_root_idx2 = get_first_smaller(array2, idx2, min_val)
    right_root_idx1 = get_first_larger(array1, idx1, max_val)
    right_root_idx2 = get_first_larger(array2, idx2, max_val)

    curr_val = array1[idx1]
    left = same_bsts(array1, array2, left_root_idx1,
                     left_root_idx2, min_val, curr_val)
    right = same_bsts(array1, array2, right_root_idx1,
                      right_root_idx2, curr_val, max_val)

    return left and right


def get_first_smaller(array, start_idx, min_val):
    for i in range(start_idx + 1, len(array)):
        if array[i] < array[start_idx] and array[i] >= min_val:
            return i
    return -1


def get_first_larger(array, start_idx, max_val):
    for i in range(start_idx + 1, len(array)):
        if array[i] >= array[start_idx] and array[i] < max_val:
            return i
    return -1
