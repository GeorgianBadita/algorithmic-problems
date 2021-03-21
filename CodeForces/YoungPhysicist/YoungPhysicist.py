def main():
    n = int(input())

    vec = None

    for _ in range(n):
        current_vec = [int(x) for x in input().split()]
        if vec == None:
            vec = [0] * len(current_vec)
        vec = [vec[i] + current_vec[i] for i in range(len(current_vec))]

    print("NO") if set(vec) != set([0]) else print("YES")


main()
