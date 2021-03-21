def main():
    username = input()

    print("CHAT WITH HER!") if len(
        set(username)) % 2 == 0 else print("IGNORE HIM!")


main()
