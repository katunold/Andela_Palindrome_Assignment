from palindrome import check_palindrome

words = []


def main():
    global run
    run = True
    while run:
        user_input = input("Insert word to test : ")
        if user_input.lower() == "exit":
            # global run
            run = False
            return
        words.insert(0, user_input)
        if len(words) == 6:
            words.pop()
        print(words)
        print(check_palindrome(user_input))


if __name__ == "__main__":
    main()
