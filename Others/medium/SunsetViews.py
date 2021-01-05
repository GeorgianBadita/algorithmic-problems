def sunsetViews(buildings, direction):
    if not buildings:
        return []

    if direction == "WEST":
        dr = 1
        curr_start = 0
        curr_end = len(buildings)
    else:
        dr = -1
        curr_start = len(buildings) - 1
        curr_end = -1

    sol = [curr_start]
    max_h = buildings[curr_start]

    while curr_start != curr_end:
        if buildings[curr_start] > max_h:
            if dr == 1:
                sol.append(curr_start)
            else:
                sol.insert(0, curr_start)
        max_h = max(max_h, buildings[curr_start])
        curr_start += dr

    return sol
