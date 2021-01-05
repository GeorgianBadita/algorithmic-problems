def gen_perms(array, perms, used, perm):
    for i in range(len(array)):
        if not used[i]:
            used[i] = True
            perm.append(array[i])
            if len(array) == len(perm):
                perms.append(perm[:])
            gen_perms(array, perms, used, perm)
            perm.pop()
            used[i] = False


def getPermutations(array):
    used = [False] * len(array)

    perm = []
    perms = []
    gen_perms(array, perms, used, perm)
    return perms


print(getPermutations([1, 2, 3]))
