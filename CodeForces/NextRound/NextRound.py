def main():
    _, k = (int(x) for x in input().split(' '))

    array = [int(x) for x in input().split(' ')]

    k_value = array[k - 1]

    cnt = 0
    for i in range(len(array)):
        if array[i] > 0 and array[i] >= k_value:
            cnt += 1
    print(cnt)


main()
