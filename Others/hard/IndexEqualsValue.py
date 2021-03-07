def indexEqualsValue(array):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

	    if array[mid] < mid:
			left = mid + 1
		elif array[mid] == mid and mid == 0:
			return mid
		elif array[mid] == mid and array[mid - 1] < mid - 1:
			return mid
		else:
			right = mid - 1

	return -1
