def arrayOfProducts(array):

    prods = [1 for _ in array]

    lft_prod = 1
    for i in range(len(array)):
        prods[i] *= lft_prod
        lft_prod *= array[i]

    rght_prod = 1
    for i in range(len(array) - 1, -1, -1):
        prods[i] *= rght_prod
        rght_prod *= array[i]

    return prods
