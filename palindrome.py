from string import ascii_letters

words = []
run = True


def check_palindrome(word):
    global val
    # empty space submitted
    if not str(word).strip():
        return "You entered nothing"
    try:
        # working with numbers submitted
        val = int(word)
        val_int = str(val)
        # reverse the number submitted
        reversed_word = val_int[::-1]
        if val_int == reversed_word:
            return "{} is a Palindrome".format(word)
        return "{} is not a Palindrome".format(word)
    except ValueError:
        val = str(word)
        del_spaces = "".join(char.lower() for char in val if char in ascii_letters)
        # reverse the word submitted
        reversed_word = del_spaces[::-1]
        # check if phrase/word is test_palindrome
        if del_spaces == reversed_word:
            return "{} is a Palindrome".format(word)
        return "{} is not a Palindrome".format(word)
