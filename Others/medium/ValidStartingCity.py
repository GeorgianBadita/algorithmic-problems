def validStartingCity(distances, fuel, mpg):
    # Write your code here.

    num_cities = len(distances)
    miles = 0

    best_index = 0
    miles_at_starting = 0

    for i in range(1, num_cities):
        dst = distances[i - 1]
        fuel_prev = fuel[i - 1]

        miles += fuel_prev * mpg - dst

        if miles < miles_at_starting:
            miles_at_starting = miles
            best_index = i
    return best_index
