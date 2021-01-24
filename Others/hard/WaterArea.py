# O(n^2) - time
# O(1) - space
def waterArea(heights):

    if not heights or len(set(heights)) == 1:
        return 0

    max_elem_poz = heights.index(max(heights))

    current_poz = 0
    while current_poz < len(heights) and heights[current_poz] == 0:
        current_poz += 1

    total_area = 0

    while current_poz < max_elem_poz:
        next_bigger_poz = current_poz
        to_decrease = 0
        for i in range(current_poz + 1, max_elem_poz + 1):
            if i != current_poz:
                to_decrease += heights[i]
            if heights[i] >= heights[current_poz]:
                next_bigger_poz = i
                to_decrease -= heights[i]
                break
        if next_bigger_poz == current_poz:
            break

        total_area += (next_bigger_poz - current_poz - 1) * \
            heights[current_poz] - to_decrease
        current_poz = next_bigger_poz

    current_poz = len(heights) - 1
    while current_poz >= 0 and heights[current_poz] == 0:
        current_poz -= 1

    while current_poz > max_elem_poz:
        next_bigger_poz = current_poz
        to_decrease = 0

        for i in range(current_poz - 1, max_elem_poz - 1, -1):
            if i != current_poz:
                to_decrease += heights[i]
            if heights[i] >= heights[current_poz]:
                next_bigger_poz = i
                to_decrease -= heights[i]
                break
        if next_bigger_poz == current_poz:
            break
        total_area += (current_poz - next_bigger_poz - 1) * \
            heights[current_poz] - to_decrease
        current_poz = next_bigger_poz

    return total_area


# O(n) - time
# O(n) - space
def waterArea1(heights):
    maxes = [0] * len(heights)

    left_max = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = left_max
        left_max = max(left_max, height)

    right_max = 0
    for i in range(len(heights) - 1, -1, -1):
        height = heights[i]
        min_height = min(right_max, maxes[i])
        if height < min_height:
            maxes[i] = min_height - height
        else:
            maxes[i] = 0
        right_max = max(right_max, height)
    return sum(maxes)


print(waterArea1([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
