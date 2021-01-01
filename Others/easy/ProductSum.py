# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    return compute_product_sum(array, 1)


def compute_product_sum(expression, nested):
    if not expression:
        return 0

    if type(expression[0]) == int:
        return expression[0] + compute_product_sum(expression[1:], nested)
    else:
        return (nested + 1) * compute_product_sum(expression[0], nested + 1) + compute_product_sum(expression[1:], nested)
