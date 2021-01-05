def powerset(array):
    arr_len = len(array)
    power_set = []

    for current_num in range(2**arr_len):
        current_set_elem = []
        bit = 0
        while 2 ** bit <= current_num:
            if current_num & (1 << bit):
                current_set_elem.append(array[bit])
            bit += 1

        power_set.append(current_set_elem)
    return power_set


def power_set2(array):
    sets = [[]]
    power_set_helper([], array, sets)
    return sets


def consistent(curr_set, new_ind):
    if not curr_set:
        return True

    return new_ind > curr_set[-1]


def power_set_helper(set_elem, array, sets):
    for i in range(0 if len(set_elem) == 0 else set_elem[-1], len(array)):
        if consistent(set_elem, i):
            set_elem.append(i)
            sets.append([array[x] for x in set_elem])
            power_set_helper(set_elem, array, sets)
            set_elem.pop()
