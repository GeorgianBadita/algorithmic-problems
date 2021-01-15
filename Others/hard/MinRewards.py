def minRewards(scores):
    rewrads = [1 for _ in range(len(scores))]

    for i in range(1, len(scores)):
        j = i - 1

        if scores[i] > scores[j]:
            rewrads[i] = 1 + rewrads[j]
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewrads[j] = max(rewrads[j], rewrads[j + 1] + 1)
                j -= 1

    return sum(rewrads)
