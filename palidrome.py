# if word is palindrome

input_word = "waabbcbbaaw"


def palindrome(input_string):
    revert_string = ""
    index = len(input_string) - 1

    while index >= 0:
        revert_string += input_string[index]
        index -= 1

    if input_string == revert_string:
        return True
    else:
        return False


if __name__ == "__main__":
    if palindrome(input_word):
        print("word is palindrome")
    else:
        print("word is not palindrome")