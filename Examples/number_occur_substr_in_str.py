"""
Write a function to count how many times the substring appears in the larger String.
"""

large_string = "abcpotqwrpot"
substring = "pot"


def count_substr_occur(input_string, input_substring):
    counter = 0
    start_index = 0
    flag = True

    while flag:

        find_index = input_string.find(input_substring, start_index)

        if find_index == -1:
            flag = False
        else:
            counter += 1
            start_index = find_index + len(input_substring)

    return counter


if __name__ == "__main__":
    print("Substring %s appears %s number(s) in the string %s" % (
    substring, count_substr_occur(large_string, substring), large_string))