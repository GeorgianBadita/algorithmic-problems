def classPhotos(redShirtHeights, blueShirtHeights):

    redShirtHeights.sort()  # we consider this as backrow
    blueShirtHeights.sort()  # we consider this as frontrow

    if redShirtHeights[0] == blueShirtHeights[0]:
        return False

    if redShirtHeights[0] < blueShirtHeights[0]:
        redShirtHeights, blueShirtHeights = blueShirtHeights, redShirtHeights

    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] <= blueShirtHeights[i]:
            return False

    return True
