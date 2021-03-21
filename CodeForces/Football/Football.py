def main():
    players = input()

    i = 0
    while i < len(players):
        num = 0
        while i + 1 < len(players) and players[i] == players[i + 1]:
            num += 1
            i += 1
        if num >= 6:
            print("YES")
            break
        if num == 0:
            i += 1
    else:
        print("NO")


main()
