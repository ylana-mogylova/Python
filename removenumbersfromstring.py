# remove numbers from a string
mixedstring = "ee32fdfdf43645kks4kjkmser445jkj4692ksj"


def remove_numbers(s):
    only_chars = ""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for char in s:
        if char not in str(numbers):
            only_chars+= char
    return only_chars

if __name__ == "__main__":
    print("only_chars =", remove_numbers(mixedstring))